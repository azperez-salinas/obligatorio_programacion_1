# Solucion Obligatorio Programación I 2024

_Autores:_ Lucas Hernandez y Ariana Perez

_Institución:_ Universidad de Montevideo, Facultad de Ingeniería

_Docente:_ Juan Andrés Gossweiler

Este proyecto es una solución para el obligatorio de Programación I.

A continuación se describe la funcionalidad de cada archivo del repositorio `obligatorio_programacion_1`.

## Archivos

### gremio.py

Este archivo contiene la clase `Gremio`, que maneja el registro de aventureros y misiones, así como la realización de misiones. Incluye métodos para registrar aventureros y misiones, realizar misiones y consultar información sobre los aventureros y misiones.

### ranger.py

Este archivo define la clase `Ranger`, que es una subclase de aventurero. Incluye atributos específicos para los Rangers, como la posibilidad de tener una mascota, y métodos para gestionar estos atributos.

### guerrero.py

Este archivo define la clase `Guerrero`, que es una subclase de aventurero. Incluye atributos específicos para los Guerreros, como la fuerza, y métodos para gestionar estos atributos.

### mago.py

Este archivo define la clase `Mago`, que es una subclase de aventurero. Incluye atributos específicos para los Magos, como el mana, y métodos para gestionar estos atributos.

### mision.py

Este archivo define la clase `Mision`, que representa una misión que los aventureros pueden realizar. Incluye atributos como el nombre, rango, recompensa y estado de completado de la misión.

### exceptions/

Este directorio contiene varias excepciones personalizadas que se utilizan en el proyecto:

- `datosInvalidos.py`: Define la excepción `DatosInvalidos`, que se lanza cuando los datos ingresados son inválidos.
- `entidadYaExiste.py`: Define la excepción `EntidadYaExiste`, que se lanza cuando se intenta registrar una entidad que ya existe.
- `entidadNoExiste.py`: Define la excepción `EntidadNoExiste`, que se lanza cuando se intenta acceder a una entidad que no existe.
- `misionYaCompletada.py`: Define la excepción `MisionYaCompletada`, que se lanza cuando se intenta realizar una misión que ya ha sido completada.

### utils/

Esta carpeta contiene la función `clear_console`, que se utiliza para limpiar la consola.

### test.py

Este archivo contiene pruebas para verificar la funcionalidad del proyecto. Incluye pruebas para registrar aventureros y misiones, realizar misiones y consultar información sobre los aventureros y misiones.

### main.py

Este archivo contiene la lógica principal del programa, incluyendo el menú principal y las opciones para registrar aventureros, registrar misiones, realizar misiones y realizar consultas adicionales donde se pueden ver los rankings segun habilidad, recompensas, etc. También maneja la interacción con el usuario a través de la consola.

## Ejecución

Para ejecutar las pruebas, simplemente ejecuta el archivo `main.py`:
