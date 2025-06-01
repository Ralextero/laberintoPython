from EstadoPuerta import EstadoPuerta


class Cerrada(EstadoPuerta):
    def abrir(self, unaPuerta):
        from Abierta import Abierta
        unaPuerta.estado = Abierta()

    def cerrar(self, unaPuerta):
        "ya cerrada"

    def entrar(self, alguien, unaPuerta):
        print(f"{alguien} ha chocado con una puerta")

    def estaAbierta(self):
        return False

    def __str__(self):
        return "Cerrada"