class Material:
    def __init__(self):
        self.nombre = "Material genérico"

    def bonificacion_defensa(self):
        pass

    def bonificacion_ataque(self):
        pass

    def __str__(self):
        return self.nombre