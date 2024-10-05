#Escribe un programa que pida la edad de una persona. Si la persona tiene
#18 años o más, debe imprimir &quot;Puedes votar&quot;. Si tiene menos de 18 años,
#debe imprimir &quot;No puedes votar&quot;.

print("PROGRAMA PARA IDENTIFICAR SI LA PERSONA PUEDE VOTAR EN ELECCIONES")

n = int(input("\n Porfavor ingrese su edad: "))

if n < 18: 
    print(f"Su edad es: {n} años, NO PUEDE VOTAR.") 
else:
    print(f"Su edad es: {n} años, PUEDES VOTAR.")