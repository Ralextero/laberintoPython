from Armamento import Armamento

class Espada(Armamento):
    def __init__(self, parte, material):
        super().__init__(parte, material)
        self.ataque_base = 3  # Ejemplo

    def bonificacion_defensa(self):
        return 0

    def bonificacion_ataque(self):
        return self.ataque_base + self.material.bonificacion_ataque()

    def esArma(self):
        return True

    def equipando(self, personaje):
        personaje.mano = self

    def __str__(self):
        return f"Espada de {self.material}"