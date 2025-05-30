from Material import Material

class Diamante(Material):
    def __init__(self):
        self.nombre = "Diamante"

    def bonificacion_defensa(self):
        return 7

    def bonificacion_ataque(self):
        return 9

    def __str__(self):
        return self.nombre