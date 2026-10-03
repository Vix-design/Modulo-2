# Validar longitud de una palabra
def validar_palabra():
    palabra = input("Escribe una palabra: ")
    longitud = len(palabra)
    if longitud < 4:
        print("Hacen falta letras")
    elif longitud <= 8:
        print("Palabra correcta")
    else:
        print("Sobran letras")

def positivo_o_negativo():
    x = int(input("Ingresa el valor de X: "))
    y = int(input("Ingresa el valor de Y: "))
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