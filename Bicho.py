from Agresivo import Agresivo
from Perezoso import Perezoso
from Ente import Ente

class Bicho(Ente):

    def __init__(self):
        super().__init__()
        self.vidas = 5
        self.poder = 1
        self.modo = Perezoso()
        self.posicion = None

    def atacar(self):
        self.juego.buscarPersonaje(self)

    def estaVivo(self):
        return self.vidas > 0
    
    def heMuerto(self):
        self.juego.terminarBicho(self)

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder=10

    def iniPerezoso(self):
        self.modo = Perezoso()
        self.poder=1

    def obtenerOrientacion(self):
        return self.posicion.obtenerOrientacion()

    def actua(self):
        self.modo.actua(self)

    def esAgresivo(self):
        return self.modo.esAgresivo()

    def esPerezoso(self):
        return self.modo.esPerezoso()
    
    def printOn(self, aStream):
        print(f"{aStream} Bicho {self.modo}")

    def __str__(self):
        return f"Bicho {self.modo}"
        
