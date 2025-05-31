from Contenedor import Contenedor

class Armario(Contenedor):

    def __init__(self):
        super().__init__()

    def esArmario(self):
        return True
    
    def __str__(self):
        return "Armario"
    
    def visitarContenedor(self, unVisitor):
        unVisitor.visitarArmario(self)

    def puedeEntrar(self,alguien):
        return alguien.esPersonaje()
    
    def entrar(self, alguien):
        if self.puedeEntrar(alguien):
            super().entrar(alguien)

    def salir(self, alguien):
        self.padre.entrar(alguien)