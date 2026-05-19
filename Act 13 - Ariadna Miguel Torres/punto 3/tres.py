#3. Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales") Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.
suma1=0
suma2=0
for i in range (1, 16):
    lista1=int(input(f"Ingrese la lista 1 en la posición n°{i}: "))
    suma1=suma1+lista1
print("Perfecto, ahora la otra lista: ")

for n in range (1, 16):
    lista2=int(input(f"Ingrese la lista 2 en la posición n°{n}: "))
    suma2=suma2+lista2

if suma1>suma2:
    print("Lista 1 mayor")
else:
    if suma2>suma1:
        print("Lista 2 mayor")
    else:
        print("Listas iguales")