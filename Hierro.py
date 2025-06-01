from Material import Material

class Hierro(Material):
    def __init__(self):
        self.nombre = "Hierro"
        self.bonificacion_ataque = 3
        self.bonificacion_defensa = 3

    def bonificacion_defensa(self):
        return self.bonificacion_defensa

    def bonificacion_ataque(self):
        return self.bonificacion_ataque

    def esHierro(self):
        return True

    def __str__(self):
        return self.nombre