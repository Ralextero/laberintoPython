from Forma import Forma

class Hexagono(Forma):

    def __init__(self):
        super().__init__()
        self.orientaciones["norte"] = None
        self.orientaciones["noreste"] = None
        self.orientaciones["sureste"] = None
        self.orientaciones["sur"] = None
        self.orientaciones["suroeste"] = None
        self.orientaciones["noroeste"] = None

    def irAlNorte(self, unEnte):
        self.orientaciones["norte"].entrar(unEnte)

    def irAlNoreste(self, unEnte):
        self.orientaciones["noreste"].entrar(unEnte)

    def irAlSureste(self, unEnte):
        self.orientaciones["sureste"].entrar(unEnte)

    def irAlSur(self, unEnte):
        self.orientaciones["sur"].entrar(unEnte)

    def irAlSuroeste(self, unEnte):
        self.orientaciones["suroeste"].entrar(unEnte)

    def irAlNoroeste(self, unEnte):
        self.orientaciones["noroeste"].entrar(unEnte)

    def __str__(self):
        return f"Hexagono"