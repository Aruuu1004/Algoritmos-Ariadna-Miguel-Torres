"""2. Desarrollar una aplicación que permita ingresar por teclado los nombres de
5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de artículos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con
un precio menor igual al valor ingresado."""

def articulosPrecios(nombre, precio):
    for x in range(5):
        valor1= input(f"Ingrese el nombre del articulo n°{x}: ")
        nombre.append(valor1)
        valor2=int(input(f"Ingrese el precio de {nombre[x]}: "))
        precio.append(valor2)
    return nombre , precio


def precioMayor(li):
    mayor=0
    for x in range(5):
        if li[x] > mayor:
            mayor= li[x]
            nomM= nombres[x]
    return nomM

def importe(lu):
    nomm=[]
    imp=int(input("Ingrese un importe: "))
    for x in range(5):
        if lu[x] < imp:
            imp=lu[x]
            nomm.append(nombres[x])
    return nomm

nombres=[]
precios=[]
lista=articulosPrecios(nombres, precios)
print(lista)
mayor=precioMayor(precios)
print(f"El articulo con mayor precio es {mayor}")
menor= importe(precios)
print(f"los articulos con precios menores son {menor} ")