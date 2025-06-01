from Llave import Llave


class InventarioMochila:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.objetos = []
        return cls._instance 

    def agregar(self, objeto):
        self.objetos.append(objeto)
        print(f"Has guardado {objeto} en la mochila.")

    def tieneLlave(self):
        return any(isinstance(obj, Llave) for obj in self.objetos)

    def contarMonedas(self):
        return sum(1 for obj in self.objetos if hasattr(obj, "esMoneda") and obj.esMoneda())

    def gastarMonedas(self, cantidad):
        gastadas = 0
        nuevos_objetos = []
        for obj in self.objetos:
            if hasattr(obj, "esMoneda") and obj.esMoneda() and gastadas < cantidad:
                gastadas += 1
                continue  # NO se añade esta moneda a la nueva lista
            nuevos_objetos.append(obj)
        self.objetos = nuevos_objetos

    def mostrar(self):
        print("Mochila:")
        for obj in self.objetos:
            print(f"  - {obj}")

    def vaciar(self):
        self.objetos.clear()