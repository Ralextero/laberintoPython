from ElementoMapa import ElementoMapa


class Llave(ElementoMapa):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def interactuar(self, personaje):
        personaje.recoger(self)
        personaje.posicion.eliminarHijo(self)
        print("Has recogido la llave.")

    def __str__(self):
        return "Llave"