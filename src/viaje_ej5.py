pregunta=True
while pregunta==True:
    distancia_km =int(input("Dime una distancia entre dos puntos cualquiera en kilometros (preferiblemente espaciales): "))  
    velocidad_kmh =int(input("Dime una velocidad en kilometros por hora: ")) 
    tiempo_horas = distancia_km / velocidad_kmh
    tiempo_dias = tiempo_horas / 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
    a=input("Quieres hacer otra simulación?, responde con s/n: ")
    if a=="s":
        pregunta=True
    elif a=="n":
        pregunta=False
    elif a!="n" and a!="s":
        print('Respueta no valida, prueba de nuevo')
        pregunta=False

#hemos puesto un while al incio de que se ejecute cuando sea verdadero, cosa que lo sera al principio, sin embargo, cuando termine el codigo, le pregutnara al usuario si quiere volver a hacerlo, si es así, seguira siendo true el codigo, si es que no o ejecuta cualquie otra respuesta, lo convertimos a false y termina el programa