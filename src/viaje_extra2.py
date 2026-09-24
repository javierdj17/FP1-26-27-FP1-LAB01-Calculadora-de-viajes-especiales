distancia_km =float(input("Dime una distancia entre dos puntos cualquiera en kilometros (preferiblemente espaciales): "))  
velocidad_kmh =float(input("Dime una velocidad en kilometros por hora: ")) 
tiempo_horas = distancia_km / velocidad_kmh
tiempo_dias = tiempo_horas // 24
semanas = tiempo_dias // 7
dias_restantes= tiempo_dias %7
print(f"Tardarías {semanas} semanas y {dias_restantes} días en llegar.")