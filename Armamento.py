from ParteCuerpo import ParteCuerpo


class Armamento(ParteCuerpo):
    def __init__(self, parte, material):
        self.parte = parte
        self.material = material

    def bonificacion_defensa(self):
        return self.parte.bonificacion_defensa() + self.material.bonificacion_defensa()
    
    def bonificacion_ataque(self):
        return self.parte.bonificacion_ataque() + self.material.bonificacion_ataque()

    def esArma(self):
        return False

    def esArmadura(self):
        return False