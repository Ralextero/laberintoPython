from Material import Material

class Oro(Material):
    def __init__(self):
        self.nombre = "Oro"
        self.bonificacion_ataque = 5
        self.bonificacion_defensa = 4

    def bonificacion_defensa(self):
        return self.bonificacion_defensa

    def bonificacion_ataque(self):
        return self.bonificacion_ataque

    def esOro(self):
        return True

    def __str__(self):
        return self.nombre