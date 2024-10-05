#5. Cambio de Variables en una Frase
print("Completa la frase con tus propias palabras o números:\n")
name = input("Introduce un nombre: ")
activity = input("Introduce una actividad que te guste: ")
place = input("Introduce un lugar: ")
age = input("Introduce una edad: ")
food = input("Introduce una comida favorita: ")
profession = input("Introduce tu profession: ")
color = input("Introduce tu color favorito: ")
hobby = input("Introduce tu hobby favorito: ")


# Frase resultante con las variables
print("\nFrase generada:")
print(name + " tiene " + age + " años y siempre ha soñado con ser " + profession + ". " +
      " Le encanta pasar el tiempo " + activity + " en " + place + " mientras disfruta de una deliciosa comida de " + food + ". " +
      " Su color favorito es " + color + " y en su tiempo libre le gusta le gusta " + hobby + ". " +
      name + " cree que cada día es una oportunidad para aprender algo nuevo y seguir creciendo.")
