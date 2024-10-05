#Escribe un programa que calcule el precio total de una compra. Si el monto
#es mayor a 1000, aplica un 10% de descuento. Si no, el precio queda igual.

print("\n PROGRAMA PARA CALCULAR EL PRECIO TOTAL DE LA COMPRA")

# Con valores de dinero es mejor trabjar con valores de tipo float(),
# pero para este ejercicio lo dejaremos en entero
precio_total = int(input("\n Digite el precio total de la compra: $" )) 

if precio_total >= 1000:
    descuento = precio_total * 0.10
    precio_final = precio_total - descuento
    print(f"\nSu compra tiene un 10% de descuento y queda en: ${precio_final}")
else:
    print(f"\nUsted no tiene descuento en esta compra")


