from Material import Material

class Diamante(Material):
    def __init__(self):
        self.nombre = "Diamante"
        self.bonificacion_ataque = 9
        self.bonificacion_defensa = 7

    def bonificacion_defensa(self):
        return self.bonificacion_defensa

    def bonificacion_ataque(self):
        return self.bonificacion_ataque

    def __str__(self):
        return self.nombre