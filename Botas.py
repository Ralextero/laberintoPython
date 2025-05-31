from ArmaduraBase import ArmaduraBase
class Botas(ArmaduraBase):
    def __init__(self, parte, material):
        super().__init__(parte, material)
        self.defensa_base = 1

    def bonificacion_defensa(self):
        return self.defensa_base + self.material.bonificacion_defensa()

    def bonificacion_ataque(self):
        return 0

    def esArmadura(self):
        return True
    
    def esBotas(self):
        return True
    
    def equipando(self,personaje):
        personaje.pies = self

    def __str__(self):
        return f"Botas de {self.material}"