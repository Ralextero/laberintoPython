from JuegoLaberinto.Laberinto.ElementoMapa import ElementoMapa

class Contenedor(ElementoMapa):

    def __init__(self):
        super().__init__()
        self.hijos = []
        self.forma = None
        self.num = None

    def agregarHijo(self, unEM):
        unEM.padre = self
        self.hijos.append(unEM)

    def agregarOrientacion(self, unaOr):
        self.forma.agregarOrientacion(unaOr)

    def eliminarHijo(self, unEM):
        try:
            self.hijos.remove(unEM)

        except ValueError:
            print(f"No existe ese objeto hijo")

    def entrar(self,alguien):
        print(f"{alguien} ha entrado en {self}")
        alguien.posicion = self
    
    def irAlEste(self,alguien):
        self.forma.irAlEste(alguien)

    def irAlOeste(self,alguien):
        self.forma.irAlOeste(alguien)

    def irAlNorte(self,alguien):
        self.forma.irAlNorte(alguien)

    def irAlSur(self,alguien):
        self.forma.irAlSur(alguien)

    def obtenerElementoOr(self,unaOr):
        return self.forma.obtenerElementoOr(unaOr)
    
    def obtenerOrientacion(self):
        return self.forma.obtenerOrientacion()
    
    def obtenerOrientaciones(self):
        return self.forma.obtenerOrientaciones()

    def ponerEnOr(self, unaOr, unEM):
        self.forma.ponerEnOr(unaOr, unEM)

    def recorrer(self, unBloque):
        unBloque(self)

        for each in self.hijos:
            each.recorrer(unBloque)

        for each in self.obtenerOrientaciones():
            each.recorrer(unBloque, self.forma)

    def __str__(self):
        return "Contenedor"