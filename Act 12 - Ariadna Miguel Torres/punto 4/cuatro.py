#4. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a. La cantidad de valores ingresados negativos.
#b. La cantidad de valores ingresados positivos.
#c. La cantidad de múltiplos de 15.
#d. El valor acumulado de los números ingresados que son pares.
valoresPositivos=0
valoresNegativos=0
Multiplos=0
valorSumaPares=0

for i in range(10):
    valor=int(input("Ingrese el valor: "))
    if valor<0:
        valoresNegativos=valoresNegativos+1
    else:
        if valor>0:
            valoresPositivos=valoresPositivos+1
    if valor%15==0 and valor>0:
        Multiplos=Multiplos+1
    if valor%2==0:
        valorSumaPares=valorSumaPares+valor

print("La cantidad de valores negativos es: ")
print(valoresNegativos)
print("La cantidad de valores positivos es: ")
print(valoresPositivos)
print("La cantidad de multiplos de 15 es: ")
print(Multiplos)
print("La suma de los valores pares es: ")
print(valorSumaPares)



