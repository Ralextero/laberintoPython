from ArmaduraBase import ArmaduraBase
class Pechera(ArmaduraBase):
    def __init__(self, parte, material):
        super().__init__(parte, material)
        self.defensa_base = 4  

    def bonificacion_defensa(self):
        return self.defensa_base + self.material.bonificacion_defensa()

    def bonificacion_ataque(self):
        return 0

    def esPechera(self):
        return True

    def esArmadura(self):
        return True

    def equipando(self, personaje):
        personaje.tronco = self

    def __str__(self):
        return f"Pechera de {self.material}"