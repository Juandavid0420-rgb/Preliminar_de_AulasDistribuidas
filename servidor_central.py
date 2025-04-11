import zmq # type: ignore
import threading
import json
import time
from random import randint

# Recursos disponibles (salones y laboratorios)
class Recursos:
    def __init__(self):
        self.salones_disponibles = 20
        self.laboratorios_disponibles = 5
        self.lock = threading.Lock()  # Para sincronizar acceso a recursos compartidos

    def asignar_aulas(self, salones_solicitados, laboratorios_solicitados):
        with self.lock:  # Sincronización para evitar conflictos
            asignacion = {"salones": 0, "laboratorios": 0, "aulas_moviles": 0, "alerta": ""}
            
            # Asignar salones
            salones_asignados = min(salones_solicitados, self.salones_disponibles)
            self.salones_disponibles -= salones_asignados
            asignacion["salones"] = salones_asignados

            # Asignar laboratorios
            laboratorios_asignados = min(laboratorios_solicitados, self.laboratorios_disponibles)
            self.laboratorios_disponibles -= laboratorios_asignados
            asignacion["laboratorios"] = laboratorios_asignados

            # Si faltan laboratorios, usar aulas móviles (salones adaptados)
            laboratorios_faltantes = laboratorios_solicitados - laboratorios_asignados
            if laboratorios_faltantes > 0:
                aulas_moviles = min(laboratorios_faltantes, self.salones_disponibles)
                self.salones_disponibles -= aulas_moviles
                asignacion["aulas_moviles"] = aulas_moviles

            # Generar alerta si no se puede cumplir la solicitud
            if (salones_solicitados > salones_asignados or 
                laboratorios_solicitados > (laboratorios_asignados + aulas_moviles)):
                asignacion["alerta"] = "No hay suficientes aulas para cumplir la solicitud."

            # Guardar asignación en un archivo
            with open("asignaciones.txt", "a") as f:
                f.write(f"{json.dumps(asignacion)}\n")

            return asignacion

# Función para manejar solicitudes de una facultad
def manejar_solicitud(socket, recursos):
    while True:
        # Recibir mensaje de una facultad
        [identity, mensaje] = socket.recv_multipart()
        solicitud = json.loads(mensaje.decode('utf-8'))
        print(f"Servidor recibió solicitud: {solicitud}")

        # Procesar solicitud
        salones_solicitados = solicitud["salones"]
        laboratorios_solicitados = solicitud["laboratorios"]
        asignacion = recursos.asignar_aulas(salones_solicitados, laboratorios_solicitados)

        # Enviar respuesta a la facultad
        respuesta = json.dumps(asignacion).encode('utf-8')
        socket.send_multipart([identity, respuesta])
        print(f"Servidor respondió: {asignacion}")

# Servidor central
def servidor_central():
    context = zmq.Context()
    socket = context.socket(zmq.ROUTER)  # Patrón ROUTER para request-reply asíncrono
    socket.bind("tcp://*:5555")

    recursos = Recursos()

    # Crear hilos para manejar solicitudes concurrentemente
    num_hilos = 3  # Número de hilos para manejar solicitudes
    for _ in range(num_hilos):
        thread = threading.Thread(target=manejar_solicitud, args=(socket, recursos))
        thread.daemon = True
        thread.start()

    print("Servidor central iniciado en puerto 5555...")
    while True:
        time.sleep(1)  # Mantener el servidor activo

if __name__ == "__main__":
    servidor_central()