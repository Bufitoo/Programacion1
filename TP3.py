#Ej 1
palabra = str(input(print("Ingrese una palabra")))
veces = str(10)
for i in range(0,10,1):
    print(i, ": ", palabra)
#Ej 2
edad = int(input(print("Ingrese su edad")))
years= 0
for i in range(1, edad):
    years: years + 1
    print("Años: ", i)
#Ej 3
num = int(input("Ingrese un numero entero positivo: "))
if num<0:
    print("El numero ingresado es negativo, por favor ingrese uno positivo")
else:
    impar = []
    for i in range(num+1):
        if (i % 2 != 0):
            impar.append(i)
impar_str = ', '.join(map(str, impar))
print("Los numeros inpares son: ", impar_str)
#Ej 4
num = int(input("Ingrese un numero entero positivo"))
if num<0:
    print("El numero ingresado es negativo, por favor ingrese uno positivo")
else:
    count = []
    for i in range(num,0,-1):
        count.append(i)
count_str = ', '.join(map(str, count))
print(count_str)
#Ej 5
cant_inv = float(input("Ingres la cantidad a invertir: "))
int_anul = float(input("Ingrese el interes anual(0,1 = 10% de interes): " ))
num_years = int(input("Ingrese la cantidad de años: "))
cap_obt = cant_inv
for i in range(num_years):
    cap_obt = (cap_obt * int_anul) + cap_obt
    print(cap_obt)
#Ej 6
num = int(input("Ingrese un numero entero positivo: "))
if num<0:
    print("El numero ingresado no es positivo")
else:
    for i in range(num+1):
        print("*"*i)
#Ej 7
for i in range(1,11):
    for j in range(1, 11):
        print("Multiplicacion de ",i,"por ",j, " es igual a: ",i*j)

#Ej 8
num = int(input("Ingrese un numero entero positivo: "))
if num<0:
    print("El numero ingresado no es positivo")
else:
    alm = []
    if num%2 == 0:
        num -= 1
        for i in range(1,num+1,2):
            alm.append(i)
    else:
        for i in range(1,num+1,2):
            alm.append(i)
tama = len(alm)
for i in range(1, tama + 1):
    inicio = 2 * i - 1
    for j in range(inicio, 0, -2):
        print(j, end=' ')
    print()
#Ej 9
password = "contraseña"

while True:
    password_input = input("Ingrese la contraseña: ")
    if password == password_input:
        print("Contraseña ingresada correctamente")
        break
    else:
        print("Contraseña incorrecta")
#Ej 10
numero = int(input("Ingrese un número entero: "))
if numero <= 1:
    print("El número no es primo.")
else:
    es_primo = 0
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = 1
            break
    if es_primo == 0:
        print("El número es primo.")
    else:
        print("El número no es primo.")
#Ej 11
palabra = input("Ingrese una palabra: ")
for i in reversed(palabra):
    print(i)
#Ej 12
frase = input("Ingrese la frase: ")
letra = input("Ingrese la letra: ")
repet = frase.count(letra)
print(f"La letra {letra} se repeite un total de: {repet}")
#Ej 13

#Ej 14
first = int(input("Ingrese el primer numero entero"))
second = int(input("Ingrese el segundo numero entero"))
pares = []
impares = []
if first%2 == 0:
    for i in range(first, second+1, 2):
        pares.append(i)
    for j in range(first+1, second+1, 2):
        impares.append(j)
else:
    for i in range(first+1, second+1, 2):
        pares.append(i)
    for j in range(first, second+1, 2):
        impares.append(j)
print(f"Los numeros pares son: {pares} y los numeros impares son: {impares}")
#Ej 15
num = int(input("Ingrese un numero mayor que 0: "))
if num <= 0:
    print("El numero ingresado es incorrecto o menor q 0")
else:
    divisores = []
    for i in range(1,num+1):
        if num%i == 0:
            divisores.append(i)
    print(f"Los divisores son: {divisores}")
#Ej 16
rep = int(input("Ingrese cuantos numeros quiere introducir: "))
contador = 0
for i in range(rep):
    num= int(input("Ingrese el numero: "))
    
    if num<0:
        contador = contador + 1
print(f"Usted a introducido una cantidad de {contador} numeros negativos")
#Ej 17
frase = input("Ingrese la frase")
vocales = {'a', 'e', 'i', 'o', 'u'}
vocales_unicas = set()

for i in frase:
    if i.lower() in vocales:
        vocales_unicas.add(i.lower())
print("Las vocales en la frase son:", ', '.join(vocales_unicas))
#Ej 18

fib = [0, 1]
for i in range(2,10):
    num_sig = fib[i-1] + fib[i-2]
    fib.append(num_sig)
for num in fib:
    print(num)

#Ej 19
tope = int(input("Ingrese la cantidad a la que quiere lograr ahorrar: "))
fondo = 0
while fondo<tope:
    deposito = int(input("Ingrese la cantidad que quiere depositar"))
    if deposito<0:
        print("El monto ingresado no puede ser menor que 0")
    else:
        fondo = fondo + deposito
print(f"Los fondos depositados fueron de: {fondo}")

#Ej 20
num = 1
acumulador = 0
while num!= 0:
    num = int(input("Ingrese un numero entero: "))
    acumulador =  num + acumulador
print(f"La sumatoria de los numeros es: {acumulador}")

#Ej 21
mayor = 0
num = 1
while num != 0:
    num = int(input("Ingrese un numero positivo: "))
    if num<0:
        print("El numero ingresado no es positivo")
    else:
        if num>mayor:
            mayor = num
print(f"El numero mayor ingresado es: {mayor}")

#Ej 22
numeros_pares = 0
while True:
    numero = int(input("Ingrese el numero entero positivo(-1 para finalizar el programa)"))
    if numero == -1:
        break
    if numero<=0:
        print("Por favor ingrese un numero positivo")
        continue
    suma = 0
    numtemp = numero
    while numtemp>0:
        suma += numtemp%10
        numtemp //= 10
    print(f"La sumatoria de los digitos del numero {numero} es: {suma}")
    if numero%2 == 0:
        numeros_pares += 1
print(f"La cantidad de numeros pares ingresados es de: {numeros_pares}")
#Ej 23 y 24
total = 0
while True:
    monto = float(input("Ingrese el monto de la compra(0 para salir)"))
    if monto == 0:
        break
    if monto<=0:
        print("Por favor ingrese un monto positivo")
        continue
    total = total + monto
if total > 1000:
    total = total - (total * 0.1)
print(f"El total del monto de las compras es de: {total}")

#Ej 25
facto = int(input("Ingrese el numero que quiere obtener su factorial: "))
factorial=0
if facto == 0:
    factorial = 1
elif facto< 0:
    print("Ingrese un numero positivo")
else:
    factorial = 1
    for i in range(1, facto+1):
        factorial *= i
print(f"El resultado es: {factorial}")


