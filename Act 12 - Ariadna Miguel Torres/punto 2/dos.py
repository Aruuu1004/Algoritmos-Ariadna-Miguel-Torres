#2. Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.

x=1
alturaFinal=0
promedio=0

a=int(input("Cuantas alturas ingresará: "))
while x<=a:
    altura=int(input("Ingrese la altura de la persona: "))
    alturaFinal=alturaFinal+altura
    x=x+1

promedio=alturaFinal/a
print("El promedio de altura de las personas es: ")
print(promedio)