from LaberintoBuilder import LaberintoBuilder
from Hexagono import Hexagono
from Noreste import Noreste
from Noroeste import Noroeste
from Sureste import Sureste
from Suroeste import Suroeste

class LaberintoBuilderHexagono(LaberintoBuilder):

    def __init__(self):
        super().__init__()

    def fabricarNoreste(self):
        return Noreste()
    
    def fabricarNoroeste(self):
        return Noroeste()
    
    def fabricarSureste(self):
        return Sureste()
    
    def fabricarSuroeste(self):
        return Suroeste()

    def fabricarForma(self):
        forma = Hexagono()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarNoreste())
        forma.agregarOrientacion(self.fabricarSureste())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarSuroeste())
        forma.agregarOrientacion(self.fabricarNoroeste())
        return forma