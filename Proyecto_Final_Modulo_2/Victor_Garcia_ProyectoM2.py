# Tupla que almacena los nombres de los cuatro cuadrantes.
# La tupla agrupa varios nombres y permite consultarlos mediante indices.
cuadrantes = ("Cuadrante I" ,"Cuadrante II" ,"Cuadrante III" ,"Cuadrante IV")

# Validar longitud de una palabra.
def validar_palabra():
# Lista par almacenar todas las palabras ingresadas.
    palabras_ingresadas = []
    # La lista almacena varios intentos, mientras ña palabara guarda un solo texto.
    palabra = input("Escribe una palabra: ")
    palabras_ingresadas.append(palabra)
    longitud = len(palabra)
    while longitud < 4 or longitud > 8:
        if longitud < 4:
            print("Hacen falta letras")
        else:
            print("Sobran letras")
        palabra = input ("Intenta nuevamente: ")
        palabras_ingresadas.append(palabra)
        longitud = len (palabra)
    print ("Palabra correcta")
    # Mostrar todas las palabras ingresadas durante la sesion.
    print("Palabras ingresadas:", palabras_ingresadas)

def positivo_o_negativo():
    #Solicitar las coordenadas X y Y al usuario.
    # X e Y son variables individuales que almacenan un valor cada una. 
    x = int(input("Ingresa el valor de X: "))
    y = int(input("Ingresa el valor de Y: "))
    #Validar que ninguna coordenada sea igual a cero
    while x == 0 or y == 0:
        print("Error: Las coordenadas no pueden ser cero")
        x = int(input("Ingresa nuevamente el valor de X: "))
        y = int(input("Ingresa nuevamente el valor de Y: "))
    #Identificar el cuadrante y consultar nombre mendiante el indice de la tupla.
    if x > 0 and y > 0:
        print(cuadrantes[0])
    elif x < 0 and y > 0:
        print(cuadrantes[1])
    elif x < 0 and y < 0:
        print(cuadrantes[2])
    elif x > 0 and y < 0:
        print(cuadrantes[3])

# Menu principal del proyecto

def menu():
    while True:
        print("\n--- PROYECTO FINAL MODULO 2 ---")
        print("1. Validar longitud de un palabra")
        print("2. Identificar cuadrante")
        print("3. Salir")

        opcion = input("Selecciona una opcion: ")
        if opcion == "1":
            validar_palabra()
        elif opcion == "2":
            positivo_o_negativo()
        elif opcion == "3":
            print("Gracias por utilizar el programa")
            break
        else:
            print("Opcion no valida, intenta nueamente")
menu()