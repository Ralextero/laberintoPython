from Material import Material

class Madera(Material):
    def __init__(self):
        self.nombre = "Madera"

    def bonificacion_defensa(self):
        return 1
    
    def bonificacion_ataque(self):
        return 1
    
    def __str__(self):
        return self.nombre