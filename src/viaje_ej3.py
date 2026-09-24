edad=int(input("Dime tu edad. "))
nivel_fisico=int(input('Dime tu nivel físico del 1 al 10. '))
if 1 <= nivel_fisico <=10:
    if edad>=18 and nivel_fisico >=5:
        print("Puedes despegar, adelante")
    else:
        if edad <18:
            print("Debes ser mayor de edad")
        else:
            print("Debes estar en mejor forma")
else:
    print("Ese nivel físico no esta disponible")


#Para evitar que se ejecute el programa cuando el usuario nos de un numero de su nivel 
#físico que no este entre 1 y 10, lo haremos con un if definiendo que entre a ese bucle
#cuando si el numero que nos de del estado físico esta entre 1 y 10, de no ser así
#el programa dira que ese no nivel físico no esta disponible