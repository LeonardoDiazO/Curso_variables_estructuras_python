"""#La estructura de las condicionales
#if -- si, elif ---segunda condicion y else: caso contario

#if
variable= int(input("Ingrese un valor"))
if  variable >=8:
    print(f"la variable {variable} si es mayor")

#ejemplo de la edad: Solicitar al usuario su edad y si es mayor a 18 años puede votar, en caso contrario no.
edad= int(input("Ingrese su edad: "))

if edad > 18:
    print(f"Ud puede votar, por que eres mayor de edad {edad}")
else:
    print(f"Ud no puede votar, por que aun eres menor de edad {edad}")
"""
"""#elif
i = int(input("Ingrese un valor: "))
        
if i > 20:
        print(f"El numero {i} es mayor que 20")
elif i > 10:
    print(f"El numero {i} es mayor que 10")
else:
    print(f"El numero {i} es menor")"""

#ejercicio 1: Escriba un programa que solicite al usuario ingresar edad y segun la edad muestre:
#1. Si tiene 18 años indicar que es menor de edad
#2. entre 18 y 65 es un adulto
#3. si es mayor a 65 es un adulto mayor

edad = int(input("Ingrese su edad por favor: "))

if edad < 18:
     print(f"Ud es menor de edad {edad}")
#elif 18 <= edad <= 65:
elif edad >=18 and edad <=65:
    print(f"Ud es un adulto {edad}")
else:
    print(f"Ud es un adulto mayor {edad}")