#Escribe un programa que pida una temperatura en grados Celsius y la
#convierta a Fahrenheit. Si la temperatura en Fahrenheit es menor que 32,
#imprime &quot;Hace frío&quot;. Si está entre 32 y 86, imprime &quot;Temperatura
#agradable&quot;. Si es mayor a 86, imprime &quot;Hace calor&quot;.

print("\nPROGRAMA PARA CONVERTIR LA TEMPERATURA DE CELSIUS A FAHRENHEIT")

celsius = int(input("\n Ingrese la temperatura en grados Celsius solo se admiten numero enteros: ")) 
   
fahrenheit = (celsius * 9/5) + 32 # FORMULA (32 °C × 9/5) + 32 = 89.6 °F
print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}°F")
    
if fahrenheit < 32:
    print("\nHace frío 🥶")
elif 32 <= fahrenheit <= 86:
    print("\nTemperatura agradable 🙂")
else:  # fahrenheit > 86
    print("\nHace calor 🥵")

# NOTA: SE PUEDE UTILIZAR EL TIPO DE DATO int() o float() pero esto depende del requerimiento,
# si se van a ingresar numero llevandolos a enteros o con sus decimales.


