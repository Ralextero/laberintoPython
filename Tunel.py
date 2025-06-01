from Hoja import Hoja

class Tunel(Hoja):

    def __init__(self):
        super().__init__()
        self.laberinto = None
    
    def esTunel(self):
        return True
    
    def aceptar(self, unVisitor):
        unVisitor.visitarTunel(self)

    def crearNuevoLaberinto(self, alguien):
        self.laberinto = alguien.juegoClonaLaberinto()
        print(f"{alguien} crea un nuevo laberinto")
        self.laberinto.entrar(alguien)

    def interactuar(self,alguien):
        self.entrar(alguien)

    def entrar(self, alguien):
        if self.laberinto is None:
            self.crearNuevoLaberinto(alguien)
        else:
            print(f"{alguien} entra en el túnel y se transporta al laberinto")
            self.laberinto.entrar(alguien)