from Armamento import Armamento

class ArmaduraBase(Armamento):
    def __init__(self, parte, material):
        super().__init__(parte, material)

    def esArmadura(self):
        return True

    def __str__(self):
        return f"{self.__class__.__name__} de {self.material}"