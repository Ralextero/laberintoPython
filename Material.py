class Material:
    def __init__(self):
        self.nombre = "Material genérico"

    def bonificacion_defensa(self):
        pass

    def bonificacion_ataque(self):
        pass

    def esMadera(self):
        return False
    
    def esHierro(self):
        return False
    
    def esDiamante(self):
        return False
    
    def esOro(self):
        return False

    def esMaterial(self):
        return True

    def __str__(self):
        return self.nombre