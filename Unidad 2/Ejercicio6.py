#Escribe un programa que pida tres números y determine cuál de ellos es el
#mayor.

print("\n PROGRAMA PARA IDENTIFICAR CUAL NUMERO ES MAYOR")

n1 = int(input("\nIngrese el primer numero entero: "))
n2 = int(input("\nIngrese el segundo numero entero: "))
n3 = int(input("\nIngrese el tercer numero entero: "))

if n1 == n2 == n3:
    print("\nLos números son todos iguales")
elif n1 > n2 and n1 > n3:
    print(f"\nEl número {n1} es mayor")
elif n2 > n1 and n2 > n3:
    print(f"\nEl número {n2} es mayor")
else:
    print(f"\nEl número {n3} es mayor")


