from ParteCuerpo import ParteCuerpo

class Manos(ParteCuerpo):

    def bonificacion_defensa(self):
        return 0

    def bonificacion_ataque(self):
        return 0
    
    def esManos(self):
        return True
    
    def __str__(self):
        return "Manos"