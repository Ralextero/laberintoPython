from Material import Material

class Hierro(Material):
    def __init__(self):
        self.nombre = "Hierro"

    def bonificacion_defensa(self):
        return 3

    def bonificacion_ataque(self):
        return 3
    
    def __str__(self):
        return self.nombre