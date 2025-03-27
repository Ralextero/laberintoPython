import time
import Modo

class Agresivo(Modo):

    def dormir(self, unBicho):
        print(f"{unBicho} duerme")
        time.sleep(1)

    def __init__(self):
        super().__init__()

    def esAgresivo(self):
        return True
    
    def __str__(self):
        return "Agresivo"