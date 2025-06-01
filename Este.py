from Orientacion import Orientacion

class Este(Orientacion):
    
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def caminar(self, unBicho):
        pos = unBicho.posicion
        pos.irAlEste(unBicho)

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.orientaciones[self.__class__.__name__.lower()] = unEM

    def obtenerElementoOrEn(self, unContenedor):
        return unContenedor.orientaciones["este"]

    def recorrer(self, unBloque, unContenedor):
        unContenedor.orientaciones["este"].recorrer(unBloque)

    def __str__(self):
        return f"Este"
    
    def calcularPosicionDesde(self, unaForma):
        unPunto = (unaForma.punto.x + 1, unaForma.punto.y)
        unaForma.orientaciones["este"].calcularPosicionDesde(unaForma, unPunto)