from Hoja import Hoja

class Tunel(Hoja):

    def esTunel(self):
        return True
    
    def aceptar(self, unVisitor):
        unVisitor.visitarTunel(self)

    def crearNuevoLaberinto(self, alguien):
        self.laberinto = alguien.juegoClonaLaberinto()
        print(f"{alguien} crea un nuevo laberinto")

    def interactuar(self,alguien):
        self.entrar(alguien)

    def entrar(self, alguien):
        if self.laberinto is None:
            self.crearNuevoLaberinto(alguien)
        else:
            print(f"{alguien} entra en el túnel y se transporta al laberinto")
            alguien.posicion = self.laberinto.entrar(alguien)