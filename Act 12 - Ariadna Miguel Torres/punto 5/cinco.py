#5. Realizar un programa que lea los lados de n triángulos, e informar:
#a. De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
#b. Cantidad de triángulos de cada tipo.
equiláteros=0
isósceles=0
escalenos=0
x=1
n=int(input("Cuantos triángulos va a ingresar?: "))
while x<=n:
    valor1=int(input(f"Ingrese el valor del lado numero 1 del triangulo n°{x}: "))
    valor2=int(input(f"Ingrese el valor del lado numero 2 del triangulo n°{x}: "))
    valor3=int(input(f"Ingrese el valor del lado numero 3 del triangulo n°{x}: "))
    if valor1==valor2 and valor2==valor3:
        print(f"El triángulo n°{x} es equilátero")
        equiláteros=equiláteros+1
    else:
        if valor1==valor2 or valor2==valor3 or valor3==valor1:
            print(f"El triángulo n°{x} es isósceles")
            isósceles=isósceles+1
        else:
            print(f"El triángulo n°{x} es escaleno")
            escalenos=escalenos+1
    x=x+1

print("La cantidad de triángulos equiláteros es: ")
print(equiláteros)
print("La cantidad de triángulos isósceles es: ")
print(isósceles)
print("La cantidad de triángulos escalenos es: ")
print(escalenos)
    