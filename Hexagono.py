from Forma import Forma

class Hexagono(Forma):

    def __init__(self):
        super().__init__()
        self.norte = None
        self.noreste = None
        self.sureste = None
        self.sur = None
        self.suroeste = None
        self.noroeste = None

    def irAlNorte(self, unEnte):
        self.norte.entrar(unEnte)

    def irAlNoreste(self, unEnte):
        self.noreste.entrar(unEnte)

    def irAlSureste(self, unEnte):
        self.sureste.entrar(unEnte)

    def irAlSur(self, unEnte):
        self.sur.entrar(unEnte)

    def irAlSuroeste(self, unEnte):
        self.suroeste.entrar(unEnte)

    def irAlNoroeste(self, unEnte):
        self.noroeste.entrar(unEnte)

    def __str__(self):
        return f"Hexagono"