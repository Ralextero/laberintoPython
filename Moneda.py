from ElementoMapa import ElementoMapa

class Moneda(ElementoMapa):
    def __str__(self):
        return "Moneda"

    def interactuar(self, personaje):
        personaje.recoger(self)
        personaje.posicion.eliminarHijo(self)
        print("Has recogido una moneda.")

    def esMoneda(self):
        return True