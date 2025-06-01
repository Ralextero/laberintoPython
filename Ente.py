from Muerto import Muerto
from Vivo import Vivo


class Ente:

    def __init__(self):
        self.vidas = None
        self.poder = None
        self.estadoEnte = Vivo()

    def esAtacadoPor(self,alguien):
        pass

    def estaVivo(self):
        return self.vidas > 0
    
    def heMuerto(self):
        self.estadoEnte = Muerto()
        self.estadoEnte.actua(self)

    def __str__(self):
        return "Ente"
    
    def atacar(self):
        self.estadoEnte.atacar(self)

    def avisar(self):
        pass

    def buscarTunel(self):
        pass

    def crearNuevoLaberinto(self):
        pass

    def juegoClonaLaberinto(self):
        if self.esBicho():
            pass
        else:
            return self.juego.clonarLaberinto()
    
    def puedeAtacar(self):
        pass

    def esPersonaje(self):
        pass

    def esBicho(self):
        pass