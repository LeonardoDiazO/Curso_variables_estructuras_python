""" Crea un bucle while con las siguientes características:
• El valor inicial de la variable x será de 0.                                      ✓  
• El valor de incremento será 1.                                                    ✓ 
• La condición de salida del bucle será mayor o igual a 30.                         ✓ 
• La ejecución se deberá romper cuando x valga 15.                                  ✓ 
• Debes imprimir la siguiente frase cada vez que se ejecute el bucle: &#39;El
valor del bucle es: &#39; + x.                                                      ✓ 
• Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.                       ✓ 
• En cada salto de ejecución, deberás mostrar los valores saltado con
este mensaje: &#39;Se saltó el valor &#39; + x &#39; de x&#39;.                     ✓ 
• Cuando se rompa la ejecución del bucle deberás mostrar un mensaje
indicándolo: &#39;Se rompió la ejecución del bucle cuando x valía &#39; + x.        ✓ """     

x = 0

while x < 30:  
    if x == 4 or x == 6 or x == 10:
        print(f"Se saltó el valor {x} de x")
        x += 1
        continue  
    
    print(f"El valor del bucle es: {x}")
    
    if x == 15:
        print(f"Se rompió la ejecución del bucle cuando x valía {x}")
        break

    x += 1 

print("Salida del While")