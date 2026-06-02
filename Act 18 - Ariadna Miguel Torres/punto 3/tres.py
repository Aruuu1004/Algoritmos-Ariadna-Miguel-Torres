"""
3. Confeccionar una función que calcule la superficie de un rectángulo y la
retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y
luego mostrar cuál de los dos tiene una superficie mayor.
"""
superficies=[]

def retornarSuperficie(v1, v2):
    sup=v1*v2
    return sup

def cargarDatos():
    lado1=int(input(f"Ingrese el ancho del rectángulo: "))
    lado2=int(input(f"Ingrese el largo del rectángulo: "))
    superficies.append(retornarSuperficie(lado1,lado2))
    print("**************************")

cargarDatos()
cargarDatos()

if superficies[0]>superficies[1]:
    print(f"El primer rectángulo posee una superficie mayor, con un valor de {superficies[0]}")
else:
    print(f"El segundo rectángulo posee una superficie mayor, con un valor de {superficies[1]}")