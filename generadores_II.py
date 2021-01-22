""" Este generador 'yield from' funciona como un for anidado.
    como si estuviesemos recorriendo una matriz de dos dimensiones
    y en vez de usar dos bucles anidados, usamos este generador """

def devuelve_ciudades( *ciudades ):
    for i in ciudades:
        #for subElemento in i:
        yield from i

ciudades_devueltas = devuelve_ciudades('Madrid', 'Barcelona', 'Valencia')

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))