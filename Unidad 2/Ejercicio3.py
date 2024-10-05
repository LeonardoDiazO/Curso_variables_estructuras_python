#Escribe un programa que pida al usuario un número entero y determine si
#es par o impar.

print("PROGRAMA PARA IDENTIFICAR NUMERO PARES O INPARES")

n = int(input("\n Porfavor ingrese un numero entero: "))

if n % 2 == 0: #Utilizamos (%) para verificar si el numero es par o impar
    print(f"El número {n} es par.") #f lo colocamos para formatear el valor de n a un string y no utilizar str()
else:
    print(f"El número {n} es impar.")

