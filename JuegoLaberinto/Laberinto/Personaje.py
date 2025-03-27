import Ente

class Personaje(Ente):

    def __init__(self):
        super().__init__()
        self.nombre = None

    def atacar(self):
        self.juego.buscarBicho(self)

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