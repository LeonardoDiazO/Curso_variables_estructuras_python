name1 = "Laura"
money1 = 10.000
name2 = "Luis"
money2 = 30.000
name3 = "Alex"
money3 = 20.000
name4 = "Rosa"
money4 = 40.000


print("\n")# genera unos espacios para mayor legibilidad desde la consola
"3. Cálculo de Promedios"
print("Calcular Promedio  x̅ ")
print("Tenemos a " + name1 + " que lleva en su bolsillo $" + str(money1))
print("Tenemos a " + name2 + " que lleva en su bolsillo $" + str(money2))
print("Tenemos a " + name3 + " que lleva en su bolsillo $" + str(money3))
print("Tenemos a " + name4 + " que lleva en su bolsillo $" + str(money4))

# Calcular el promedio
total_money = money1 + money2 + money3 + money4  # Suma de todo el dinero
number_of_people = 4  # Usar Decimal para el número de personas
average_money = total_money / number_of_people  # Calcular el promedio como Decimal

# Imprimir el promedio
print("\nEl promedio de dinero que llevan en los bolsillos es: x̅ = $" + str(average_money))  # No se necesita redondear
