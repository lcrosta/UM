"""Escribir un programa que pregunte al usuario la fecha de su nacimiento 
en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
El programa debe funcionar, también, cuando el día o el mes se introduzcan con un solo carácter."""

fe = input("Ingrese fecha de nacimiento")

if len(fe) == 10:
    print("Dia: ", fe[0:2])
    print("Mes: ", fe[3:5])
    print("Año: ", fe[6:])
elif len(fe) == 9:
    print("Dia: ", fe[0:1])
    print("Mes: ", fe[2:4])
    print("Año: ", fe[5:])
