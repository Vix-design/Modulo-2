# Validar longitud de una palabra
def validar_palabra():
    palabra = input("Escribe una palabra: ")
    longitud = len(palabra)
    while longitud < 4 or longitud > 8:
        if longitud < 4:
            print("Hacen falta letras")
        else:
            print("Sobran letras")
        palabra = input ("Intenta nuevamente")
        longitud = len (palabra)
    print ("Palabra correcta")

def positivo_o_negativo():
    x = int(input("Ingresa el valor de X: "))
    y = int(input("Ingresa el valor de Y: "))
    while x == 0 or y == 0:
        print("Error: Las coordenadas no pueden ser cero")
        x = int(input("Ingresa nuevamente el valor de X: "))
        y = int(input("Ingresa nuevamente el valor de Y: "))

    if x > 0 and y > 0:
        print("Cuadrante I")
    elif x < 0 and y > 0:
        print("Cuadrante II")
    elif x < 0 and y < 0:
        print("Cuadrante III")
    elif x > 0 and y < 0:
        print("Cuadrante IV")
positivo_o_negativo()
validar_palabra()