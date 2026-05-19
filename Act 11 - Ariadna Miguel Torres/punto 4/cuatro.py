#4. Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número tiene uno o dos dígitos. (Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

num=int(input("Ingrese un número positivo de uno o dos digitos: "))
if num<10 and num>0:
    print("El número es de un digito")
else:
    if num>9 and num<100:
        print("El número es de dos digitos")
    else:
        if num<0:
            print("Valor incorrecto,ingrese uno positivo")
        else:
            print("Valor incorrecto, ingrese uno de uno o dos digitos")