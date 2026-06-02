"""
1. Desarrollar un programa que solicite la carga de tres valores y muestre el
menor. Desde el bloque principal del programa llamar 2 veces a dicha
función (sin utilizar una estructura repetitiva)
"""

menor=0

def cargarValores():
    num1=int(input("Ingrese el primer valor: "))
    num2=int(input("Ingrese el segundo valor: "))
    num3=int(input("Ingrese el tercer valor: "))
    print(f"el número menor es {encontrarMenor(num1, num2, num3)}")
    print(f"el número menor es {encontrarMenor(num1, num2, num3)}")


def encontrarMenor(v1, v2, v3):
    if v1<v2 and v1<v3:
        menor=v1
    else:
        if v2<v1 and v2<v3:
            menor=v2
        else:
            menor=v3
    return menor


cargarValores()