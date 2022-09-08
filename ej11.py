"""Haz un programa que muestre la tabla de multiplicar de un número introducido por teclado por el usuario."""

num = int(input("Ingrese un número para calcular su tabla"))

for i in range(0,11,1):
    print(i*num)
    print("\n")