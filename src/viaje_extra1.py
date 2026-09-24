x=int(input('Introduce la distancia total en kilometros que quieres, realizar: '))
print('vaya, nuestra nave solo es capaz de hacer 150000 km sin parar, tendremos que parar en las siguientes.')
paradas=0
for i in range(150000,x,150000):
    print('parada en el km: ',i)
    paradas +=1
print('El total de paradas que vamos a realizar son: ', paradas, 'Buen Viaje!')
