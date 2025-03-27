from Ente import Ente

class Personaje(Ente):

    def __init__(self,unaCadena):
        super().__init__()
        self.vidas = 1000
        self.nombre = unaCadena

    def atacar(self):
        self.juego.buscarBicho()
        print(f"{self} ataca")

    def heMuerto(self):
        self.juego.muerePersonaje()

    def irAlEste(self):
        self.posicion.irAlEste(self)

    def irAlNorte(self):
        self.posicion.irAlNorte(self)

    def irAlOeste(self):
        self.posicion.irAlOeste(self)
    
    def irAlSur(self):
        self.posicion.irAlSur(self)

    def __str__(self):
        return f"Personaje {self.nombre}"