"""Escribe un programa que muestre los números
pares positivos entre 2 y un número cualquiera que introduzca el usuario por teclado"""

num = int(input("Ingresar número límite"))

for i in range (2,num+1,1):
    if i%2 == 0:
        print(i)