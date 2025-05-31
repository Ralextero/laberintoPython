from ParteCuerpo import ParteCuerpo

class Tronco(ParteCuerpo):
    def bonificacion_defensa(self):
        return 0

    def bonificacion_ataque(self):
        return 0

    def esTronco(self):
        return True

    def __str__(self):
        return "Tronco"