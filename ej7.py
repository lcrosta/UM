"""Implementa un programa que muestre todos los múltiplos de 6 entre 6 y 150, ambos inclusive."""

for x in range (0,151,6):
    if x%2 == 0 and x != 0:
        print(x)
