#comentario es de una linea
"""hola esto es un mensaje
de comentario de
varias lineas"""

#variable -- > almacenar un dato
#nombre, valor, tipo de dato numeros enteros int,
#decimales float, cadenas string

nombre_apellido = "Salvador" # variable de tipo cadena
edad = 4 # variable de tipo entero
estatura = 1.05 #variable de tipo decimal
estudia = True # variable que almacena un valor booleano

print(nombre_apellido)

print("la edad es: ", edad)

print(f"la estatura de {nombre_apellido} es: {estatura}")

#ejercicio
num1 = 34
num2 = 29

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
divi = num1 / num2

print(f"El valor de la suma es: {suma},de la resta es: {resta}, de la multi es {multi} y la divi es: {divi}")

numero = int(input("ingrese un numero por favor: "))
numero_2 = int(input("ingrese otro numero por favor: "))

suma = numero + numero_2
resta = numero - numero_2
multi = numero * numero_2
divi = numero / numero_2

print(f"El valor de la suma es: {suma},de la resta es: {resta}, de la multi es {multi} y la divi es: {divi}")