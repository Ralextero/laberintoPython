from Material import Material

class Oro(Material):
    def __init__(self):
        self.nombre = "Oro"

    def bonificacion_defensa(self):
        return 4

    def bonificacion_ataque(self):
        return 5
    
    def __str__(self):
        return self.nombre