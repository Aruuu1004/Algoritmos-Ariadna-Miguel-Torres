"""
1-
Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
"""

def cargarDatos():
    lista=[]
    for x in range(5):
        valor=int(input(f"Ingrese el entero n°{x}: "))
        lista.append(valor)
    return lista

def mayorMenor(li):
    mayor=li[0]
    menor=li[0]
    aux=0
    for aux in li:
        if aux>mayor:
            mayor=aux
    for aux in li:
        if aux<menor:
            menor=aux
    return (mayor, menor)


Datos=cargarDatos()
Carga=mayorMenor(Datos)
print(f"Valores dentro de la tupla: {Carga}")
mayor,menor=Carga
print("Valores fuera de tupla: ")
print(f"El valor mayor de la lista es {mayor}")
print(f"El valor menor de la lista es {menor}")