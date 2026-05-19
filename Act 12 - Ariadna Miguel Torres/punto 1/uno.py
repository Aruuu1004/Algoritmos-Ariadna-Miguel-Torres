#1. Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.
contadorMayor=0
contadorMenor=0

for i in range(10):
    valor=int(input("Ingrese la nota del alumno: "))
    if valor<0 or valor>10:
        print("Valor incompatible")
    else:
        if valor==7 or valor>7:
            contadorMayor=int(contadorMayor+1)
        else:
            contadorMenor=(contadorMenor+1)
print("La cantidad de alumnos con una nota mayor o igual a 7 es: ")
print(contadorMayor)
print("La cantidad de alumnos con una nota menor a 7 es: ")
print(contadorMenor)