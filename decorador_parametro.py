def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
        print('Vamos a realizar un calculo: ')

        funcion_parametro(*args)
        #Acciones adicionales que decoran

        print('Hemos terminado el cálculo.')
    return funcion_interior


@funcion_decoradora
def suma( num1, num2 ):
    print( num1 + num2 )

@funcion_decoradora
def resta( num1, num2 ):
    print( num1 - num2 )

suma(7,5)
resta(12,10)