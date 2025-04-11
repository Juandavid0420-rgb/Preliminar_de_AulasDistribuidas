import zmq # type: ignore
import json
import threading
import time
from random import randint

# Función para manejar solicitudes de programas académicos
def manejar_programas(socket_programas, solicitudes_programas):
    while True:
        mensaje = socket_programas.recv_json()
        print(f"Facultad recibió solicitud de programa: {mensaje}")
        solicitudes_programas.append(mensaje)
        # Enviar confirmación al programa
        socket_programas.send_json({"status": "Solicitud recibida"})

# Facultad
def facultad(nombre_facultad):
    context = zmq.Context()

    # Socket para comunicarse con los programas (request-reply síncrono)
    socket_programas = context.socket(zmq.REP)
    socket_programas.bind(f"tcp://*:5556")  # Puerto para programas

    # Socket para comunicarse con el servidor central (request-reply asíncrono)
    socket_servidor = context.socket(zmq.DEALER)
    socket_servidor.setsockopt_string(zmq.IDENTITY, nombre_facultad)
    socket_servidor.connect("tcp://localhost:5555")

    solicitudes_programas = []

    # Hilo para recibir solicitudes de los programas
    thread_programas = threading.Thread(target=manejar_programas, args=(socket_programas, solicitudes_programas))
    thread_programas.daemon = True
    thread_programas.start()

    print(f"Facultad {nombre_facultad} iniciada...")

    # Enviar solicitudes al servidor central cada 5 segundos
    while True:
        time.sleep(5)  # Simula un ciclo de envío periódico
        if solicitudes_programas:
            # Consolidar solicitudes de los programas
            total_salones = sum(prog["salones"] for prog in solicitudes_programas)
            total_laboratorios = sum(prog["laboratorios"] for prog in solicitudes_programas)
            solicitud = {
                "facultad": nombre_facultad,
                "salones": total_salones,
                "laboratorios": total_laboratorios
            }

            # Enviar solicitud al servidor
            socket_servidor.send_json(solicitud)
            print(f"Facultad {nombre_facultad} envió solicitud: {solicitud}")

            # Recibir respuesta del servidor
            respuesta = socket_servidor.recv_json()
            print(f"Facultad {nombre_facultad} recibió respuesta: {respuesta}")

            # Guardar la asignación en un archivo
            with open(f"asignaciones_{nombre_facultad}.txt", "a") as f:
                f.write(f"{json.dumps(respuesta)}\n")

            # Limpiar solicitudes procesadas
            solicitudes_programas.clear()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python facultad.py <nombre_facultad>")
        sys.exit(1)
    facultad(sys.argv[1])