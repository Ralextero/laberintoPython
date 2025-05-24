from LaberintoBuilder import LaberintoBuilder
from Octogono import Octogono

class LaberintoBuilderOctogono(LaberintoBuilder):

    def __init__(self):
        super().__init__()

    def fabricarNoreste(self):
        from Noreste import Noreste
        return Noreste()
    
    def fabricarNoroeste(self):
        from Noroeste import Noroeste
        return Noroeste()
    
    def fabricarSureste(self):
        from Sureste import Sureste
        return Sureste()
    
    def fabricarSuroeste(self):
        from Suroeste import Suroeste
        return Suroeste()

    def fabricarForma(self):
        forma = Octogono()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarNoreste())
        forma.agregarOrientacion(self.fabricarEste())
        forma.agregarOrientacion(self.fabricarSureste())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarSuroeste())
        forma.agregarOrientacion(self.fabricarOeste())
        forma.agregarOrientacion(self.fabricarNoroeste())
        return forma