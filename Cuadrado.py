from Forma import Forma

class Cuadrado(Forma):

    def __init__(self):
        super().__init__()
        self.orientaciones["norte"] = None
        self.orientaciones["este"] = None
        self.orientaciones["sur"] = None
        self.orientaciones["oeste"] = None

    def irAlEste(self, unEnte):
        self.orientaciones["este"].entrar(unEnte)

    def irAlNorte(self, unEnte):
        self.orientaciones["norte"].entrar(unEnte)

    def irAlOeste(self, unEnte):
        self.orientaciones["oeste"].entrar(unEnte)

    def irAlSur(self, unEnte):
        self.orientaciones["sur"].entrar(unEnte)

    def __str__(self):
        return f"Cuadrado"

    