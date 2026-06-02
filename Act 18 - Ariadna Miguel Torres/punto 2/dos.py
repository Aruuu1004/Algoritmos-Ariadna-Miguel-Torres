"""2. Confeccionar una función que reciba tres enteros y los muestre ordenados
de menor a mayor. En otra función solicitar la carga de 3 enteros por
teclado y proceder a llamar a la primer función definida."""

x=0
aux=0
def ListaOrdenada(v1, v2, v3):
    list=[v1, v2, v3]
    for x in range(2):
        if list[x]>list[x+1]:
            aux=list[x]
            list[x]=list[x+1]
            list[x+1]=aux
    return list
        

def cargarDatos():
    num1=int(input("Ingrese el primer valor: "))
    num2=int(input("Ingrese el segundo valor: "))
    num3=int(input("Ingrese el tercer valor: "))
    print(f"La lista ordenada será: {ListaOrdenada(num1, num2, num3)}")

cargarDatos()