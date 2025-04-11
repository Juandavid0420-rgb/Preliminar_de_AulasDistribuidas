import zmq # type: ignore
import json
import time
from random import randint

def programa_academico(nombre_programa, puerto_facultad):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://localhost:{puerto_facultad}")

    print(f"Programa {nombre_programa} iniciado...")

    while True:
        # Generar solicitud aleatoria
        solicitud = {
            "programa": nombre_programa,
            "salones": randint(5, 7),
            "laboratorios": randint(1, 3)
        }

        # Enviar solicitud a la facultad
        socket.send_json(solicitud)
        print(f"Programa {nombre_programa} envió solicitud: {solicitud}")

        # Recibir confirmación de la facultad
        respuesta = socket.recv_json()
        print(f"Programa {nombre_programa} recibió confirmación: {respuesta}")

        time.sleep(10)  # Enviar solicitudes cada 10 segundos

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Uso: python programa_academico.py <nombre_programa> <puerto_facultad>")
        sys.exit(1)
    programa_academico(sys.argv[1], sys.argv[2])