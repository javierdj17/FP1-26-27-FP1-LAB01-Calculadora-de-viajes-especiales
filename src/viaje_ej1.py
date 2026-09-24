distancia_km = 38440000  # distancia Tierra - Luna
velocidad_kmh = 50000
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas / 24
tiempo_semanas = tiempo_dias // 7
dias_sobrantes = tiempo_dias % 7
print(f"Tardarías {tiempo_semanas} semanas y {dias_sobrantes} días en llegar.")

#se muestran numeros decimales en la primera opción ya que la operación / nos devuelve una división EXACTA con sus numeros decimales,
#mientras que la operación // nos devuelve solo la parte entera de esa división.