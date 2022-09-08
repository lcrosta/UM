"""Escribe un programa que pregunte el nombre del usuario en la consola y un número 
entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido."""

nom = (input("Ingrese su nombre: "))
num = int(input("Ingrese el número: "))

for i in range (0,num,1):
    print(nom)
    