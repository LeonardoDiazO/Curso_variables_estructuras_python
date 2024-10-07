#4. Contar cuántos números impares hay en un rango

num = int(input("Digite un numero para poder definir un rango: "))

cont_impar = 0

for i in range(1, num + 1):
    if i % 2 != 0:  
        cont_impar += 1

print(f"En el rango de 1 a {num} hay {cont_impar} números impares.")