from Puerta import Puerta

class PuertaConLlave(Puerta):
    def abrir(self, personaje):
        if personaje.inventario.tieneLlave():
            super().abrir()
            print("Has abierto la puerta con la llave.")
        else:
            print("Necesitas una llave para abrir esta puerta.")