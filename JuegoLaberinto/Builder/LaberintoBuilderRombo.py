from JuegoLaberinto.Builder import LaberintoBuilder
from JuegoLaberinto.Laberinto import Rombo


class LaberintoBuilderRombo(LaberintoBuilder):

    def __init__(self):
        super().__init__()

    def fabricarForma(self):
        forma = Rombo()
        forma.agregarOrientacion(self.fabricarNoreste())
        forma.agregarOrientacion(self.fabricarSureste())
        forma.agregarOrientacion(self.fabricarSuroeste())
        forma.agregarOrientacion(self.fabricarNoroeste())
        return forma