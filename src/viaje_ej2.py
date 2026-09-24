distancia_km =int(input("Dime una distancia entre dos puntos cualquiera en kilometros (preferiblemente espaciales): "))  
velocidad_kmh =int(input("Dime una velocidad en kilometros por hora: ")) 
tiempo_horas = distancia_km / velocidad_kmh
tiempo_dias = tiempo_horas / 24
print(f"Tardarías {tiempo_dias} días en llegar.")

#Ahora en este caso pedimos una distancia y una velocidad y calcularemos cuantos dias se tarda en llegar