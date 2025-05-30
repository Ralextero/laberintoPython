import random
from Contenedor import Contenedor
from Manos import Manos
from Cabeza import Cabeza
from Tronco import Tronco
from Piernas import Piernas
from Pies import Pies
from Diamante import Diamante
from Hierro import Hierro
from Oro import Oro

class Cofre(Contenedor):
    def __init__(self, posibles_objetos):
        super().__init__()
        self.posibles_objetos = posibles_objetos  # Lista de clases de objetos posibles
        materiales = [Diamante, Hierro, Oro]
        partes = {
            "Espada": Manos,
            "Casco": Cabeza,
            "Pechera": Tronco,
            "Pantalones": Piernas,
            "Botas": Pies
        }
        for _ in range(3):
            clase = random.choice(self.posibles_objetos)
            if clase.__name__ in partes:
                parte = partes[clase.__name__]()
                material = random.choice(materiales)()
                objeto = clase(parte, material)
            else:
                objeto = clase()
            self.agregarHijo(objeto)

    def interactuar(self, personaje):
        if not self.hijos:
            print("El cofre está vacío.")
            return
        print("¡Has abierto un cofre y encontrado:")
        for obj in self.hijos:
            print(f"  - {obj}")

    def __str__(self):
        return "Cofre"