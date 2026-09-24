distancia_km = 225000000
#velocidad_kmh = 5000

for i in range(10000,50000,10000):
    tiempo_horas = distancia_km / i
    tiempo_dias = tiempo_horas / 24 
    semanas = tiempo_dias // 7
    dias_restantes = tiempo_dias % 7
    print(f"velocidad: {i}km/h --> tiempos: {semanas} semanas y {dias_restantes} dias")

#lo haremos con un for i in range y dentro de ese for ponemos el primer valor sera donde empieze, el segundo donde acaba, y el tercero (opcional), los saltos que va pegando, en este caso de 10.000 en 10.000