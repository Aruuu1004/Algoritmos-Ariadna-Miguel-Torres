"""
4. Confeccionar una función que reciba una serie de edades y me retorne la
cantidad que son mayores o iguales a 18 (como mínimo se envía un entero
a la función)
"""

edad=[20,15,17,19,18,20]

def edades(le):
    contador=0
    for x in range(len(le)):
        if le[x] >= 18:
            contador=contador+1
    return contador


print(f"hay {edades(edad)} edades mayores o iguales a 18")