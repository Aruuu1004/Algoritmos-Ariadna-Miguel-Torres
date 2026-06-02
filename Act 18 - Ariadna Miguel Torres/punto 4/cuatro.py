"""
4. Plantear una función que reciba un string en mayúsculas o minúsculas y
retorne la cantidad de letras "a" o "A".
"""
x=0

def letras(v1):
    contador=0
    for x in range(len(v1)):
        if "a" in v1[x]:
            contador=contador+1
        if "A" in v1[x]:
            contador=contador+1
    return contador

def cargarString():
    string=(input("Ingrese su cadena: "))
    print(f"La cantidad de letras a o A son {letras(string)}")

cargarString()