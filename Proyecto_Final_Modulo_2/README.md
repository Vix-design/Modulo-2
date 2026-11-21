# Proyecto Final - Módulo 2

# Descripción
Este proyecto es un programa desarrollado en Python que integra dos funcionalidades mediante un menú interactivo, el mismo permite validar la longitud de una palabra e identificar el cuadrante al que pertenece un punto dentro del plano cartesiano.

# Funcionalidades

# 1. Validar longitud de una palabra
- Solicita al usuario ingresar una palabra.
- Utiliza `len()` para contar sus caracteres.
- Si tiene menos de 4 caracteres, muestra "Hacen falta letras".
- Si tiene entre 4 y 8 caracteres, muestra "Palabra correcta".
- Si tiene más de 8 caracteres, muestra "Sobran letras".
- Permite volver a ingresar una palabra hasta cumplir la condición.

# 2. Identificar cuadrante
- Solicita los valores de X y Y.
- Valida que ninguna coordenada sea igual a cero.
- Identifica el cuadrante correspondiente mediante condiciones `if`, `elif` y `else`.

Los cuatro cuadrantes considerados son:
- Cuadrante I: X positiva, Y positiva.
- Cuadrante II: X negativa, Y positiva.
- Cuadrante III: X negativa, Y negativa.
- Cuadrante IV: X positiva, Y negativa.

# 3. Menú principal
El programa cuenta con un menú que permite seleccionar las dos funcionalidades o salir del programa.

# Tecnologías utilizadas
- Python 3
- Visual Studio Code

## Ejecución del programa

1. Seleccionar la carpeta del proyecto en Visual Studio Code.
2. Abrir la terminal.
3. Ejecutar el siguiente comando:

```bash
python3 Victor_Garcia_ProyectoM2.py
```

4. Seleccionar una opción del menú y seguir las instrucciones.

## Reflexión personal

## Reflexión personal

Durante el desarrollo de este proyecto pude comprender mejor cómo las estructuras de control ayudan a organizar la lógica de un programa y permiten tomar decisiones de acuerdo con los datos ingresados por el usuario.

El uso de las estructuras condicionales `if`, `elif` y `else` me permitió evaluar diferentes situaciones, como validar la longitud de una palabra e identificar correctamente los cuatro cuadrantes del plano cartesiano.

También aprendí a utilizar ciclos `while` para repetir instrucciones cuando los datos ingresados no cumplen con las condiciones establecidas. Esto permitió que el programa fuera más interactivo y evitara continuar con coordenadas iguales a cero.

Finalmente, integrar las dos funcionalidades mediante un menú me ayudó a comprender cómo organizar diferentes procesos dentro de un mismo programa. Este proyecto reforzó mis conocimientos sobre variables, condiciones, ciclos, funciones y colecciones de datos, y me permitió desarrollar una mejor forma de analizar y resolver problemas mediante Python.