
from operator import truediv

suma = 0
contador = 0
num = 1
while num != 0:
    num =  int(input("Ingrese número: "))
    if num == 0:
        break
    suma = suma + num
    contador = contador + 1

    
print(suma)
print(contador)

print("Promedio: ", suma/(contador))

