#Escribe un programa que pida una calificación numérica (entre 0 y 100) y
#devuelva una calificación basada en la siguiente escala:
# 90 - 100: A
# 80 - 89: B
# 70 - 79: C
# 60 - 69: D
# Menos de 60: F

print("\n Programa para califaciones")
n = int(input("\n Ingrese la calificacion entre estos valores (0 - 100): "))

if n < 0 or n > 100:
    print("\nEl valor no es válido. Debe estar entre 0 y 100.")
elif n <= 60:
    print("\nSu calificacion numerica es: "+ str(n)+ " y su calificacion alfabética es: (F)" )
elif n >= 60 and n <= 69:
    print("\nSu calificacion numerica es: "+ str(n) + " y su calificacion alfabética es: (D)" )
elif n >= 69 and n <= 79:
    print("\nSu calificacion numerica es: "+ str(n) + " y su calificacion alfabética es: (C)" )
elif n >= 79 and n <= 89:
    print("\nSu calificacion numerica es: "+ str(n) + " y su calificacion alfabética es: (B)" )
elif n >= 89 and n <= 100:
    print("\nSu calificacion numerica es: "+ str(n) + " y su calificacion alfabética es: (A)" )



