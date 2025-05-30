from Agresivo import Agresivo
from Perezoso import Perezoso
from Ente import Ente

class Bicho(Ente):

    def __init__(self):
        super().__init__()
        self.modo = Perezoso()

    def esAtacadoPor(self, alguien):
        print(f"{self} es atacado por {alguien}")
        self.vidas = max(0, self.vidas - alguien.ataque_total())
        print(f"Vidas: {self.vidas}")
        if self.vidas <= 0:
            self.heMuerto()

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder=30

    def iniPerezoso(self):
        self.modo = Perezoso()
        self.poder=5

    def obtenerOrientacion(self):
        return self.posicion.obtenerOrientacion()

    def actua(self):
        self.estadoEnte.actua(self)

    def esAgresivo(self):
        return self.modo.esAgresivo()

    def esPerezoso(self):
        return self.modo.esPerezoso()

    def __str__(self):
        return f"Bicho {self.modo}"
    
    def avisar(self):
        self.juego.terminarBicho(self)

    def buscarTunel(self):
        self.modo.buscarTunelBicho(self)
        
    def puedeActuar(self):
        self.modo.actua(self)

    def puedeAtacar(self):
        self.juego.buscarPersonaje(self)