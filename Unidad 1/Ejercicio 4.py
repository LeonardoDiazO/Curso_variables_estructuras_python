# 4. Mini Proyecto de Programación
print("\n")
name = input("¿Cual es su nombre? :")
favorites = input("¿Que te gusta hacer? :")
age = input("¿Que edad tienes? :")
food = input("¿Cual es tu comida favorita ? :")

print("\n")
respuesta = input("¿Quieres imprimir un texto con los datos que me suministraste datos? (si/no):")
print("\n")
if respuesta.lower() == "si": #tomamos todos las posibles respuestas que puede dar el usuario, al momento de escribir
    print("Hola mi nombre es, " + name + " tengo " + age + " años," + 
          " mi comida favorita es " + food + " y mi pasatiempo favorito es " + favorites) 
elif respuesta.lower() == "no":
    print("Gracias por darnos tu apreciación")
else:
    print("No es valida tu respuesta.")

