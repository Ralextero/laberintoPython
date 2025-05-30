from ArmaduraBase import ArmaduraBase
class Pantalones(ArmaduraBase):
    def __init__(self, parte, material):
        super().__init__(parte, material)
        self.defensa_base = 3  # Ejemplo

    def bonificacion_defensa(self):
        return self.defensa_base + self.material.bonificacion_defensa()

    def bonificacion_ataque(self):
        return 0

    def esArmadura(self):
        return True