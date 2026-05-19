#1. Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuántos de esos nombres tienen 5 o más caracteres y mostrarlo.

lista=["Juan", "Josefina", "Carolina", "Martin", "Rosa"]
cincoMas=0
x=0

while x<4:
    if len(lista[x])>=5:
        cincoMas=cincoMas+1
    x=x+1

print("La cantidad de nombres con 5 o más caracteres es: ")
print(cincoMas)