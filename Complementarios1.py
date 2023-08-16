#Realizo el nombramiento de todas las variables a utilizar y le asigno su valor
numero = 4
numero2 = 8.4
nombre = "Nazareno"
precio = 100
descuento = 0.25
cadena = str("Hola a todos")
precio = 120
nombre = str("Nazareno")
apellido = str(" Herrera")
edad = 25
altura = 1.83
mNombre = "NAZARENO"
miNombre = "nazareno"

#Realizo el nombramiento de las variables que llevaran acabo una operacion en ellas
suma = numero + numero2
resta = numero - numero2
multipicacion = numero * numero2
division = numero/numero2

longitud = len(cadena) #Obtengo la longitud de la variable cadena
precio_final = precio*descuento #Calculo el precio final de un producto
nombre_completo = nombre + apellido #Realzio la concatenacion 

edad += 5 #Incremento el valor de una variable
edad -= 10 #Dismunucion del valor de la variable

altura *= 4 #Multiplicacion de una variable
altura /=10 #Divison de la variable

mNombre_lower = mNombre.lower() #Conversion a minuscula
miNombre_upper = mNombre.upper() #Conversion a mayuscula

#Muestro los valores finales que son pedidos

print("Se muestra las operaciones: " , "\nSuma: ",suma,"\nResta: ",resta,"\nMultiplicación: ",multipicacion,"\nDivisión: ",division) #Procedo a mostrar las operaciones anteriores
print("El precio final es: ", precio_final, "\nLa longitudo de la cadena es de: ", longitud )
print("El nombre completo es: ",nombre_completo)
print("Resultado de edad despues de modificarla: " ,edad)
print ("Resultado de la altura: ", altura)
print("Nombre convertido en minuscula: ",mNombre_lower)
print("Nombre convertido en mayuscula: ",miNombre_upper)





