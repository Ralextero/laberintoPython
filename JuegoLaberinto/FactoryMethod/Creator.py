from JuegoLaberinto.Laberinto.Bicho import Bicho
from JuegoLaberinto.Laberinto.Bomba import Bomba
from JuegoLaberinto.Laberinto.Pared import Pared
from JuegoLaberinto.Laberinto.Puerta import Puerta
from JuegoLaberinto.Laberinto.Habitacion import Habitacion
from JuegoLaberinto.Laberinto.Laberinto import Laberinto
from JuegoLaberinto.Laberinto.Este import Este
from JuegoLaberinto.Laberinto.Oeste import Oeste
from JuegoLaberinto.Laberinto.Norte import Norte
from JuegoLaberinto.Laberinto.Sur import Sur
from JuegoLaberinto.Laberinto.Agresivo import Agresivo
from JuegoLaberinto.Laberinto.Perezoso import Perezoso
from JuegoLaberinto.Laberinto.Juego import Juego

class Creator:

    def fabricarBichoAgresivo(self):
        bicho = Bicho()
        bicho.modo = Agresivo() 
        bicho.vida = 5
        bicho.poder = 5
        return bicho
    
    def fabricarBichoAgresivo(self, posicion):
        bicho = Bicho()
        bicho.modo = Agresivo()
        bicho.vida = 5
        bicho.poder = 5
        bicho.posicion = posicion
        return
    
    def fabricarBichoPerezoso(self):
        bicho = Bicho()
        bicho.modo = Perezoso() 
        bicho.vida = 1
        bicho.poder = 1
        return bicho
    
    def fabricarBichoPerezoso(self, posicion):
        bicho = Bicho()
        bicho.modo = Perezoso()
        bicho.vida = 1
        bicho.poder = 1
        bicho.posicion = posicion
        return
    
    def cambiarAModoAgresivo(self, bicho):
        bicho.modo = Agresivo()
        bicho.vida = 5
        bicho.poder = 10

    def cambiarAModoPerezoso(self, bicho):
        bicho.modo = Perezoso()
        bicho.vida = 1
        bicho.poder = 1

    def fabricarBomba(self):
        return Bomba()
    
    def fabricarEste(self):
        return Este()
    
    def fabricarOeste(self):
        return Oeste()
    
    def fabricarNorte(self):
        return Norte()
    
    def fabricarSur(self):
        return Sur()
    
    def fabricarHabitacion(self, unNum):
        hab = Habitacion(unNum)
        hab.agregarOrientacion(self.fabricarEste())
        hab.agregarOrientacion(self.fabricarOeste())
        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(self.fabricarSur())
        for each in hab.obtenerOrientaciones():
            each.ponerEnOr(self.fabricarPared(), each)
        return hab
    
    def fabricarPared(self):
        return Pared()
    
    def fabricarPuerta(self):
        return Puerta()
    
    def fabricarJuego(self):
        return Juego()
    
    def fabricarLaberinto(self):
        return Laberinto()