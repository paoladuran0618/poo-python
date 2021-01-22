""" Usando generadores.
    Yield Genera numeros en cada iteracion
    es como una lista dinámica.
"""

def funcion_generadora(lim):
    num = 1
    while num < lim:
        yield num*2
        num += 1

retorna_pares = funcion_generadora(10)

for i in retorna_pares:
    print(i)
