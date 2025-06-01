from Material import Material

class Madera(Material):
    def __init__(self):
        self.nombre = "Madera"
        self.bonificacion_ataque = 1
        self.bonificacion_defensa = 1

    def bonificacion_defensa(self):
        return self.bonificacion_defensa

    def bonificacion_ataque(self):
        return self.bonificacion_ataque

    def esMadera(self):
        return True

    def __str__(self):
        return self.nombre