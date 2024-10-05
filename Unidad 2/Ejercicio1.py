#Escribe un programa que pida al usuario un número entero. Si el número es
#positivo, el programa debe imprimir &quot;Positivo&quot;. Si es negativo, debe imprimir
#&quot;Negativo&quot;. Si es cero, debe imprimir &quot;Es cero&quot;.

print("\n Programa para identificar numeros")
n = int(input("\n Ingrese un numero entero: "))
if n > 0:
    print(str(n) + " Es un numero positivo")
elif n < 0:
    print(str(n) + " Es un numero negativo")
else:
    print(str(n) + "No es un numero valido.")

