from Puerta import Puerta

class PuertaConLlave(Puerta):
    def abrir(self, personaje = None):
        if personaje is None:
            print("Puerta especial, no se abre así.")
            return
        elif personaje.mochila.tieneLlave():
            super().abrir()
        else:
            print("Necesitas una llave para abrir esta puerta.")

    def esPuertaConLlave(self):
        return True
    
    def __str__(self):
        return "Puerta con llave"