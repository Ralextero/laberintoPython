from Laberinto.Laberinto import *

class Creator:

    def fabricarBichoAgresivo(self):
        bicho = Bicho()
        bicho.set_modo(Agresivo()) 
        bicho.set_vida(5)
        bicho.set_poder(5)
        return bicho
    
    def fabricarBichoPerezoso(self):
        bicho = Bicho()
        bicho.set_modo(Perezoso()) 
        bicho.set_vida(1)
        bicho.set_poder(1)
        return bicho
    
    def cambiarAModoAgresivo(self, bicho):
        bicho.set_modo(Agresivo())
        bicho.set_vida(5)
        bicho.set_poder(10)

    def cambiarAModoPerezoso(self, bicho):
        bicho.set_modo(Perezoso())
        bicho.set_vida(1)
        bicho.set_poder(1)

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
        for orientacion in hab.get_orientaciones():
            orientacion.ponerEnOr(self.fabricarPared(), orientacion)
        return hab
    
    def fabricarPared(self):
        return Pared()
    
    def fabricarPuerta(self):
        return Puerta()
    
    def fabricarJuego(self):
        return Juego()
    
    def fabricarLaberinto(self):
        return Laberinto()
    
class CreatorB(Creator):

    def fabricarPared(self):
        return ParedBomba()