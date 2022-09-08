"""Haz un programa que vaya leyendo números hasta que el usuario introduzca un número negativo. 
En ese momento, el programa mostrará por pantalla el número mayor de cuantos ha visto."""

num = 0
max = 0

while num >= 0:
    num = int(input("Ingrese un número: "))
    if num > max:
        max = num
    
print("Número más alto ingresado: ", max)