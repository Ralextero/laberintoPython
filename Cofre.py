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
        posibles_objetos  # Lista de clases de objetos posibles
        materiales = [Diamante, Hierro, Oro]
        partes = {
            "Espada": Manos,
            "Casco": Cabeza,
            "Pechera": Tronco,
            "Pantalones": Piernas,
            "Botas": Pies
        }
        for _ in range(3):
            clase = random.choice(posibles_objetos)
            if clase.__name__ in partes:
                parte = partes[clase.__name__]()
                material = random.choice(materiales)()
                objeto = clase(parte, material)
            else:
                objeto = clase()
            self.agregarHijo(objeto)

    def esCofre(self):
        return True

    def mostrar_menu(self):
        if not self.hijos:
            print("El cofre está vacío.")
            return
        print("\nEl cofre contiene:")
        for idx, obj in enumerate(self.hijos, 1):
            print(f"{idx}. {obj}")
        print(f"{len(self.hijos)+1}. Salir")

    def recoger_objeto(self, personaje, indice):
        if 0 <= indice < len(self.hijos):
            objeto = self.hijos[indice]
            personaje.recoger(objeto)
            self.eliminarHijo(objeto)
            print(f"Has recogido {objeto}.")
            return True
        else:
            print("Opción no válida.")
            return False

    def recorrer(self, unBloque):
        pass

    def entrar(self, alguien):
        return

    def __str__(self):
        return "Cofre"