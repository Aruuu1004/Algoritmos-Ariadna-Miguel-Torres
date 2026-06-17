"""
2-
Confeccionar un programa con las siguientes funciones:
1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos
valores
2)Una función que reciba como parámetro dos tuplas con los nombres y sueldos
de empleados y muestre el nombre del empleado con sueldo mayor.
En el bloque principal del programa llamar dos veces a la función de carga y
seguidamente llamar a la función que muestra el nombre de empleado con sueldo
mayor.
# bloque principal
empleado1=cargar_empleado()
empleado2=cargar_empleado()
mayor_sueldo(empleado1,empleado2)
"""

def cargarDatos():
    nombre=input("Ingrese el nombre del empleado: ")
    sueldo=int(input(f"Ingrese el sueldo de {nombre}: "))
    return (nombre, sueldo)

def mayor(valor1, valor2):
    empleadoMayor=valor1
    if valor2[1]>empleadoMayor[1]:
        empleadoMayor=valor2
    print(f"El nombre del empleado con mayor sueldo es {empleadoMayor[0]}, con un sueldo de {empleadoMayor[1]}")




empleado1=cargarDatos()
empleado2=cargarDatos()
mayor(empleado1,empleado2)
