# Simulador de Asignación de Recursos Académicos 📚✨

Bienvenido al proyecto preliminar de un simulador para asignar salones y laboratorios a programas académicos en una universidad. Este README explica el propósito, la estructura y los detalles del diseño inicial. 🚀

## Descripción del Proyecto 🏫

Este simulador modela la asignación de recursos (salones y laboratorios) a programas académicos de dos facultades ficticias. Cada programa solicita una cantidad aleatoria de recursos, y un servidor central con recursos limitados realiza las asignaciones. Los resultados se guardan en un archivo de texto para su revisión. 📝

### Características Principales 🌟
- **Facultades y Programas**: Simula 2 facultades, cada una con 2 programas académicos.
- **Solicitudes Aleatorias**:
  - Cada programa solicita entre **5 y 7 salones** 🏢.
  - Cada programa solicita entre **1 y 3 laboratorios** 🧪.
- **Recursos Disponibles**: 
  - Servidor central con **20 salones** y **5 laboratorios**.
- **Almacenamiento**: Las asignaciones se guardan en un **archivo de texto** 📄.
- **Diseño Simplificado**: No incluye tolerancia a fallas ni servidor réplica (puede implementarse en futuras versiones 🔄).

## Requisitos 📋
- Lenguaje de programación: [Especificar según implementación, e.g., Python, Java, etc.] 🖥️
- Generador de números aleatorios para simular solicitudes.
- Sistema de archivos para almacenar las asignaciones.

## Estructura del Proyecto 🗂️
```plaintext
simulador_recursos/
├── main.py                 # Script principal para ejecutar la simulación 🎮
├── asignador.py            # Lógica de asignación de recursos ⚙️
├── datos/
│   └── asignaciones.txt    # Archivo de salida con resultados 📄
└── README.md               # Este archivo 📖
```

## Cómo Ejecutar 🚀
1. Clona este repositorio:
   ```bash
   git clone [URL-del-repositorio]
2. Navega al directorio del proyecto:
   ```bash
   cd simulador_recursos

3. Ejecuta el script principal:
   ```bash
   python main.py
   
4. Revisa el archivo
   ```bash
   datos/asignaciones.txt
  para ver los resultados. 📊

  ## Ejemplo de Salida 📄
  El archivo asignaciones.txt podría verse así:
  ```plaintext
Facultad 1 - Programa 1: 6 salones, 2 laboratorios asignados
Facultad 1 - Programa 2: 5 salones, 1 laboratorio asignado
Facultad 2 - Programa 1: 7 salones, 3 laboratorios asignados
Facultad 2 - Programa 2: 2 salones, 0 laboratorios asignados (insuficientes)
```

## Limitaciones 🚧
- No hay tolerancia a fallas ni redundancia (servidor réplica).
- Los recursos son limitados y podrían no satisfacer todas las solicitudes.
- Diseño preliminar, sujeto a mejoras futuras.
## Futuras Mejoras 🔮
- Implementar un servidor réplica para tolerancia a fallas 🛡️.
- Agregar validaciones más robustas para las solicitudes.
- Incluir una interfaz gráfica para visualizar las asignaciones 📈.
- Permitir configuraciones personalizadas de facultades y programas.
## Contribuciones 🤝
¡Las ideas y mejoras son bienvenidas! Si deseas contribuir:

## Haz un fork del repositorio.
Crea una rama para tus cambios (git checkout -b mi-mejora).
Envía un pull request con tus modificaciones. 🌈
