from ParteCuerpo import ParteCuerpo

class Piernas(ParteCuerpo):
    from ParteCuerpo import ParteCuerpo

class Piernas(ParteCuerpo):
    def bonificacion_defensa(self):
        return 0

    def bonificacion_ataque(self):
        return 0

    def esPiernas(self):
        return True

    def __str__(self):
        return "Piernas"