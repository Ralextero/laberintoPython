from JuegoLaberinto.Laberinto import Agresivo, Bicho, Bomba, Cuadrado, Este, Habitacion, Juego, Laberinto, Norte, Oeste, Perezoso, Puerta, Sur, Tunel


class LaberintoBuilder:

    def __init__(self):
        self.laberinto = None
        self.juego = None

    def fabricarBichoAgresivo(self):
        bicho = Bicho()
        bicho.modo = Agresivo()
        bicho.vidas = 5
        bicho.poder = 5
        return bicho
    
    def fabricarBichoAgresivo(self, unaHab):
        bicho = Bicho()
        bicho.modo = Agresivo()
        bicho.posicion = unaHab
        bicho.vidas = 5
        bicho.poder = 5
        return bicho
    
    def fabricarBichoPerezoso(self):
        bicho = Bicho()
        bicho.modo = Perezoso()
        bicho.vidas = 5
        bicho.poder = 1
        return bicho
    
    def fabricarBichoPerezoso(self, unaHab):
        bicho = Bicho()
        bicho.modo = Perezoso()
        bicho.posicion = unaHab
        bicho.vidas = 5
        bicho.poder = 1
        return bicho
    
    def fabricarBichoModo(self, strModo, unNum):
    
        hab = self.laberinto.obtenerHabitacion(unNum)

        bicho = getattr(self, f"fabricarBicho{strModo.capitalize()}")()

        hab.entrar(bicho)

        self.juego.agregarBicho(bicho)

    def fabricarBombaEn(self, unContenedor):
        bmb = Bomba()
        unContenedor.agregarHijo(bmb)

    def fabricarEste(self):
        return Este()
    
    def fabricarNorte(self):
        return Norte()
    
    def fabricarOeste(self):
        return Oeste()
    
    def fabricarSur(self):
        return Sur()
    
    def fabricarForma(self):
        forma = Cuadrado()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarEste())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarOeste())
        return forma
    
    def fabricarHabitacion(self, unNum):
    
        hab = Habitacion()
        hab.num = unNum

        hab.forma = self.fabricarForma()

        for each in hab.obtenerOrientaciones():
            hab.ponerEnOr(each, self.fabricarPared())

        self.laberinto.agregarHabitacion(hab)

        return hab
    
    def fabricarJuego(self):
        self.juego= Juego()
        self.juego.laberinto= self.laberinto

    def fabricarLaberinto(self):
        self.laberinto= Laberinto()

    def fabricarPuertaL1(self, num1, strOr1, num2, strOr2):
    
        hab1 = self.laberinto.obtenerHabitacion(num1)
        hab2 = self.laberinto.obtenerHabitacion(num2)

        objOr1 = getattr(self, f"fabricar{strOr1.capitalize()}")()  # Ejemplo: fabricarNorte
        objOr2 = getattr(self, f"fabricar{strOr2.capitalize()}")()

        pt = Puerta()
        pt.lado1 = hab1
        pt.lado2 = hab2

        hab1.ponerEnOr(objOr1, pt)
        hab2.ponerEnOr(objOr2, pt)

    def fabricarTunel(self, unContenedor):
        tunel = Tunel()
        unContenedor.agregarHijo(tunel)

    def obtenerJuego(self):
        return self.juego