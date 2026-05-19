#2. En un banco se procesan datos de las cuentas corrientes de sus clientes. De cada cuenta corriente se conoce: número de cuenta y saldo actual. El ingreso de datos debe finalizar al ingresar un valor negativo en el número de cuenta. Se pide confeccionar un programa que lea los datos de las cuentas corrientes e informe:
#● a) De cada cuenta: número de cuenta y estado de la cuenta según su saldo, sabiendo que:
#○ Estado de la cuenta:
#○ “Acreedor” si el saldo es > 0.
#○ “Deudor” si el saldo es < 0.
#○ “Nulo” si el saldo es = 0.
#● b) La suma total de los saldos acreedores.

sumaAcreedores=0
numCuenta=int(input("Ingrese su número de cuenta (para finalizar, ponga un valor negativo): "))
while numCuenta>0:
    saldo=int(input(f"Ingrese el saldo de la cuenta {numCuenta}: "))
    if saldo>0:
        print(f"La cuenta n°{numCuenta} es acreedora")
        sumaAcreedores=sumaAcreedores+saldo
    else:
        if saldo<0:
            print(f"La cuenta n°{numCuenta} es deudora")
        else:
            print(f"La cuenta n°{numCuenta} es nula")
    numCuenta=int(input("Ingrese su número de cuenta (para finalizar, ponga un valor negativo): "))

print("El total de la suma de los saldos acreedores es: ")
print(sumaAcreedores)

