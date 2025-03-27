from JuegoLaberinto.FactoryMethod.Creator import Creator
from JuegoLaberinto.Laberinto.ParedBomba import ParedBomba

class CreatorB(Creator):

    def fabricarPared(self):
        return ParedBomba()