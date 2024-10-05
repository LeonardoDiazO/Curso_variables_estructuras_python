# 6. Experimentos de Datos
print("Encuesta: ¿Cuál es tu lenguaje de programación favorito?\n")

print("Elige entre estas opciones, solo ingresa el número de la opción: ")
print("1 - JavaScript")
print("2 - HTML")
print("3 - Python")
print("4 - SQL")
print("5 - Java")
print("6 - C#")

lenguajes = []

for i in range(6):
    respuesta = input("Persona " + str(i+1) + ", ¿cuál es tu lenguaje de programación favorito?: ")
    
    if respuesta == "1":
        lenguajes.append("JavaScript")
    elif respuesta == "2":
        lenguajes.append("HTML")
    elif respuesta == "3":
        lenguajes.append("Python")
    elif respuesta == "4":
        lenguajes.append("SQL")
    elif respuesta == "5":
        lenguajes.append("Java")
    elif respuesta == "6":
        lenguajes.append("C#")
    else:
        print("Opción no válida. Se omitirá esta entrada.")

conteo_lenguajes = {}

for lenguaje in lenguajes:
    if lenguaje in conteo_lenguajes:
        conteo_lenguajes[lenguaje] += 1
    else:
        conteo_lenguajes[lenguaje] = 1

print("\nResultados de la encuesta:")
for lenguaje, conteo in conteo_lenguajes.items():
    print("El lenguaje " + lenguaje + " fue elegido por " + str(conteo) + " persona(s).")
