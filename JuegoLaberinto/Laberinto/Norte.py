from JuegoLaberinto.Laberinto.Orientacion import Orientacion

class Norte(Orientacion):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance    

    def caminar(self, unBicho):
        pos = unBicho.posicion
        pos.irAlNorte(unBicho)

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.norte = unEM

    def obtenerElementoOrEn(self, unContenedor):
        return unContenedor.norte
    
    def recorrer(self, unBloque, unContenedor):
        unContenedor.norte.recorrer(unBloque)

    def __str__(self):
        return f"Norte"