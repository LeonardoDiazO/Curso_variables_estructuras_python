#2. Crear una tabla de multiplicar (del 1 al 10)
print("\nProgrma para tablas de multiplicar (del 1 al 10)")
num = int(input("Ingrese el numero de la tabla a la cual quiere visualizar, rango (1 - 10): "))

for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")