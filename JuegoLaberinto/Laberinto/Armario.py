from JuegoLaberinto.Laberinto.Contenedor import Contenedor

class Armario(Contenedor):

    def __init__(self):
        super().__init__()

    def esArmario(self):
        return True
    
    def __str__(self):
        return "Armario"