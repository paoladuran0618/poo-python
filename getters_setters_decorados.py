class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    #debe tener el mismo nombre de la variable que vamos a ingresar con el setter ej. region -> @region.setter
    @region.setter
    def setter_region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError('Laregion {} no esta en la lista'.format(region)) 

if __name__ == '__main__':
    casilla = CasillaDeVotacion(123, ['Ciudad de Mexico', 'Morelos'])
    print(casilla.region)
    casilla.setter_region = 'Ciudad de Mexico'
    print(casilla.region)