#1. En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

x=1
empleadosMenor=0
empleadosMayor=0
importe=0
n=int(input("Cuantos empleados ingresará?: "))
while x<=n:
    sueldo=int(input(f"Ingrese el sueldo del empleado n°{x}: "))
    if sueldo>=100 and sueldo<=300:
        empleadosMenor=empleadosMenor+1
    else:
        if sueldo>300 and sueldo<=500:
            empleadosMayor=empleadosMayor+1
        else:
            if sueldo<100 or sueldo>500:
                print("Valor incompatible, ingrese un sueldo entre 100 y 500")
    importe=importe+sueldo
    x=x+1

print("La cantidad de empleados que cobran entre $100 y $300 es: ")
print(empleadosMenor)
print("La cantidad de empleados que cobran mas de $300 es: ")
print(empleadosMayor)
print("El importe que gasta la empresa en sueldos es: ")
print(importe)


