class ElementoMapa:

    def __init__(self):
        self.padre = None

    def entrar(self):
        pass

    def entrar(self, alguien):
        pass

    def esArmario(self):
        pass

    def esBomba(self):
        pass

    def esHabitacion(self):
        pass

    def esLaberinto(self):
        pass

    def esPared(self):
        pass

    def esPuerta(self):
        pass

    def recorrer(self, unBloque):
        unBloque(self)

    def __str__(self):
        return "ElementoMapa"