from ParteCuerpo import ParteCuerpo


class Cabeza(ParteCuerpo):
    def bonificacion_defensa(self):
        return 0

    def bonificacion_ataque(self):
        return 0
    
    def esCabeza(self):
        return True
    
    def __str__(self):
        return "Cabeza"