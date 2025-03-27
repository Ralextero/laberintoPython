from JuegoLaberinto.Laberinto.Contenedor import Contenedor

class Laberinto(Contenedor):

    def __init__(self):
        super().__init__()

    def abrirPuertas(self):
        def abrirSiEsPuerta(elemento):
            if elemento.esPuerta():
                elemento.abrir()
        self.recorrer(abrirSiEsPuerta)

    def cerrarPuertas(self):
        def cerrarSiEsPuerta(elemento):
            if elemento.esPuerta():
                elemento.cerrar()
        self.recorrer(cerrarSiEsPuerta)

    def entrar(self):
        hab1 = self.obtenerHabitacion(1)
        hab1.entrar()
        return "Estas en un laberinto"
    
    def esLaberinto(self):
        return True
    
    def agregarHabitacion(self, unaHabitacion):
        self.hijos.append(unaHabitacion)

    def eliminarHabitacion(self, unaHabitacion):
        try:
            self.hijos.remove(unaHabitacion)

        except ValueError:
            print(f"No existe ese objeto habitacion")

    def obtenerHabitacion(self, unNum):
        for habitacion in self.hijos:
            if habitacion.num == unNum:
                return habitacion
        return None
    
    def recorrer(self, unBloque):
        unBloque(self)
        for hijo in self.hijos:
            self.recorrer(unBloque)

    def printOn(self, aStream):
        print(f"{aStream} Laberinto")

    def __str__(self):
        return "Laberinto"