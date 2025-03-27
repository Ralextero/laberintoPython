from ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):

    def abrir(self):
        self.abierta = True
        print(f"{self} ha sido abierta.")

    def cerrar(self):
        self.abierta = False
        print(f"{self} ha sido cerrada.")

    def entrar(self, alguien):
        if self.abierta:
            if alguien.posicion == self.lado1:
              self.lado2.entrar(alguien)
              print(f"{alguien} ha entrado en {self.lado2}")
            else:
                self.lado1.entrar(alguien)
                print(f"{alguien} ha entrado en {self.lado1}")
        else:
             print(f"{alguien} se ha chocado con la puerta.")

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

    def __str__(self):
        return f"Puerta - {self.lado1.num} - {self.lado2.num}"