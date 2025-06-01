from Orientacion import Orientacion

class Noroeste(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def caminar(self, unBicho):
        pos = unBicho.posicion
        pos.irAlNoroeste(unBicho)

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.orientaciones[self.__class__.__name__.lower()] = unEM

    def obtenerElementoOrEn(self, unContenedor):
        return unContenedor.orientaciones["noroeste"]

    def recorrer(self, unBloque, unContenedor):
        unContenedor.orientaciones["noroeste"].recorrer(unBloque)

    def calcularPosicionDesde(self, unaForma):
        unPunto = (unaForma.punto.x - 1, unaForma.punto.y - 1)
        unaForma.orientaciones["noroeste"].calcularPosicionDesde(unaForma, unPunto)

    def __str__(self):
        return f"Noroeste"