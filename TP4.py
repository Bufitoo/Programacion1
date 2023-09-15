"""#Ej 1
entrada = True
x = 1
print("RESULTADOS:")
while x <= 15:
    if(x== 4 or x == 6 or x == 10):
        print(f"Se salto el valor {x} de x")
    elif(x == 15):
        print(f"Se interumpio la ejecucion del bucle cuando x valia: {x}")
        break
    else:
        print(x)
    x =  x + 1

#Ej 2
lineas = []
entrada = True
while entrada:
    linea = input("Ingrese una línea (o deje en blanco para finalizar): ")
    if not linea:
        entrada = False
        break
    lineas.append(linea.upper())
for linea in lineas:
    print(linea)


#Ej 3
saldo = 0
while True:
    operacion = input("Introduce una operación (D para depósito, R para retiro, o deja en blanco para terminar): ")
    if not operacion:
        break
    tipo, cantidad = operacion.split()
    cantidad = int(cantidad)
    if tipo == "D":
        saldo += cantidad
    elif tipo == "R":
        if saldo<cantidad:
            print("Saldo insuficiente para retirar")
        else:
            saldo -= cantidad
print("Su saldo es de: ",saldo)

#Ej 4
# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.
# Imprimir la cantidad total de números primos ingresados.
# Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.
accumulator = 0
while True:
    num_into = int(input("Ingrese el numero(0 para finalizar el programa)"))
    var = True
    if num_into>1:
        for i in range(2, int(num_into**0.5) + 1):
            if num_into % i == 0:
                var = False
        if var == True:
            accumulator += 1
    elif num_into == 0:
        break
    else:
        print("El numero ingresado tiene que ser mayor a 1")
print(f"Los numero primos ingresados fueron: {accumulator}")
#Ej 5
# Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.
# Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
while True:
    year_first = int(input("Ingrese el primero año: "))
    year_second = int(input("Ingrese el segundo año: "))
    if year_second>1 and year_first>1:
        break
for i in range(year_first, year_second+1):
    if ((i%4==0 and i%100!=0)or(i%400 == 0))and i%10 == 0:
        print(i)
#Ej 6
# Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. Utiliza la declaración continue para omitir los números impares.
for i in range(1,21):
    if i%2==0:
        print(i)
    else:
        continue
#Ej 7
#6.	Crea una lista de números y utiliza un bucle for para encontrar un número específico. Cuando encuentres el número, usa break para salir del bucle.
accumulator = [10 , 20 , 30 , 45 , 55, 68]
num_input = int(input("Ingrese el numero que quiere buscar: "))
for i, elemnto in enumerate(accumulator):
    if elemnto == num_input:
        print(f"El elemento {num_input} se encuentra en el índice {i}")
        break"""
#Ej 8
# Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). Utiliza un bucle while para permitir al usuario seleccionar 
# una opción. Si el usuario ingresa "0", utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).
while True:
    print("MENU DE COMPRA")
    print("Eliga una ocpion")
    option = int(input(" 1-Carnes \n 2-Lacteos \n 3-Bebidas \n 0-Salir \n"))
    if(option>=1 and option<4):
        print(f"Elegiste la opcion {option}")
        break
    elif option==0:
        print("Saliste del Menu de compra")
        break
    else:  
        print("La opcion elegida no se encuentra")

