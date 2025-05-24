from Forma import Forma

class Octogono(Forma):

    def __init__(self):
        super().__init__()
        self.norte = None
        self.noreste = None
        self.este = None
        self.sureste = None
        self.sur = None
        self.suroeste = None
        self.oeste = None
        self.noroeste = None

    def irAlNorte(self, unEnte):
        self.norte.entrar(unEnte)

    def irAlNoreste(self, unEnte):
        self.noreste.entrar(unEnte)

    def irAlEste(self, unEnte):
        self.este.entrar(unEnte)

    def irAlSureste(self, unEnte):
        self.sureste.entrar(unEnte)

    def irAlSur(self, unEnte):
        self.sur.entrar(unEnte)

    def irAlSuroeste(self, unEnte):
        self.suroeste.entrar(unEnte)

    def irAlOeste(self, unEnte):
        self.oeste.entrar(unEnte)

    def irAlNoroeste(self, unEnte):
        self.noroeste.entrar(unEnte)

    def __str__(self):
        return f"Octogono"