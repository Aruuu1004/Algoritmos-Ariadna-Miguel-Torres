#4. Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano. Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

a=1
primerCuadrante=0
segundoCuadrante=0
tercerCuadrante=0
cuartoCuadrante=0

n=int(input("Cuantos puntos va a ingresar?: "))
while a<=n:
    x=int(input(f"Ingrese el valor x del punto n°{a}: "))
    y=int(input(f"Ingrese el valor y del punto n°{a}: "))
    if x<0 and y>0:
        primerCuadrante=primerCuadrante+1
    else:
        if x>0 and y>0:
            segundoCuadrante=segundoCuadrante+1
        else:
            if x>0 and y<0:
                tercerCuadrante=tercerCuadrante+1
            else:
                cuartoCuadrante=cuartoCuadrante+1
    a=a+1

print("La cantidad de puntos en el primer cuadrante es: ")
print(primerCuadrante)
print("La cantidad de puntos en el segundo cuadrante es: ")
print(segundoCuadrante)
print("La cantidad de puntos en el tercer cuadrante es: ")
print(tercerCuadrante)
print("La cantidad de puntos en el cuarto cuadrante es: ")
print(cuartoCuadrante)