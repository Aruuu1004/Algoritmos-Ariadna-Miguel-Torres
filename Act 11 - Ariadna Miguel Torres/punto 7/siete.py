#7. Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule e informe su rango de variación (debe mostrar el mayor y el menor de ellos)

num1=int(input("Ingrese el primer valor: "))
num2=int(input("Ingrese el segundo valor: "))
num3=int(input("Ingrese el tercer valor: "))

if num1>num2 and num1>num3:
    numMayor=num1
else:
    if num2>num1 and num2>num3:
        numMayor=num2
    else:
        if num3>num1 and num3>num2:
            numMayor=num3


if num1<num2 and num1<num3:
    numMenor=num1
else:
    if num2<num1 and num2<num3:
        numMenor=num2
    else:
        if num3<num1 and num3<num2:
            numMenor=num3

variacion=numMayor-numMenor
print("Entre los números hay una variación de: ")
print(variacion)
print("El número mayor es: ")
print(numMayor)
print("El número menor es: ")
print(numMenor)