"""Los teléfonos de una empresa tienen el siguiente formato 
prefijo-número-extension donde el prefijo es el código del país +34, 
y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir
un programa que pregunte por un número de teléfono con este formato y
muestre por pantalla el número de teléfono sin el prefijo y la extensión."""

num1 = (input("Ingrese el número de telefono de la compañia completo: "))

larg = len(num1)

num2 = num1[4:larg-3] 


print(num2)