from errno import EDEADLK


ed1 = input("Ingrese la edad de la primer persona ")
ed2 = input("Ingrese la edad de la segunda persona ")
if ed1<ed2:
    print("La primer persona es más joven")
elif ed2<ed1:
    print("La segunda persona es más joven")
else:
    print("Ambas personas tienen la misma edad")