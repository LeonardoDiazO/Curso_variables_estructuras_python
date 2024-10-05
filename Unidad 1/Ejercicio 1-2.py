"""1. Juego de Asignación de Variables"""

name = "Leonardo"  # Variable de tipo cadena 
last_name = "Diaz"  # Variable de tipo cadena
email = "maximun_neo@hotmail.com"  # Variable de tipo cadena 
phone = 3016805257  # Variable de tipo entero 
birth_date = "1988-11-22"  # Variable de tipo cadena en formato 'YYYY-MM-DD'
active = True  # Variable de tipo booleano
country = "Barranquilla" 
ocupation = "Desarrollador"


"2. Historias con Variables"
print("Historias con Variables:")
print("Hola, mi nombre es " + name + " " + last_name + ",")
print("tengo una edad de " + str(2024 - int(birth_date.split('-')[0])) + " años,")
print("y me desempeño como " + ocupation + " para una empresa de Colombia que se llama Hypersoft"".")
print("Me encuentro viviendo en " + country+"."+ "\n "+" ¿ Que es lo que mas me gusta? ")
print("*** Trabajar")
print("*** Estudiar" + " ✔ " + str(active)) #str convierte la variable en un string
print("Me apaciona seguir aprendiendo apesar de que aveces tengo otras ocupaciones." )
print("FIRMA: "+name+" "+ last_name +" "+"correo:"+ email + " " + "Telefono:"+ str(phone))
