import ElementoMapa

class Puerta(ElementoMapa):

    def abrir(self):
        self.abierta = True

    def cerrar(self):
        self.abierta = False

    def entrar(self, alguien):
        if self.abierta:
            if alguien.posicion == self.lado1:
              self.lado2.entrar(alguien)
            else:
                self.lado1.entrar(alguien)
        else:
             print(f"Te has chocado con la puerta.")

    def esPuerta(self):
        return True

    def __init__(self):
        super().__init__()
        self.abierta = False
        self.lado1 = None
        self.lado2 = None

    def estaAbierta(self):
        return self.abierta
    
    def printOn(self, aStream):
        print(f"{aStream} Puerta - {self.lado1.num} - {self.lado2.num} - {self.abierta}")