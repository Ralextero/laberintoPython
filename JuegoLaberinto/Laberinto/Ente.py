class Ente:

    def __init__(self):
        self.vidas = None
        self.poder = None
        self.posicion = None
        self.juego = None

    def esAtacadoPor(self,alguien):
        print(f"{self} es atacado por {alguien}")
        self.vidas -= alguien.poder
        print(f"Vidas: {self.vidas}")
        if self.vidas <= 0:
            self.heMuerto()

    def estaVivo(self):
        return self.vidas > 0
    
    def heMuerto(self):
        pass

    def __init__(self):
        self.vidas = 5
        self.poder = 1

    def __str__(self):
        return "Ente"