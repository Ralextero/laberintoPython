from random import random


class Modo:

    def __init__(self):
        pass

    def actua(self, unBicho):
        self.dormir(unBicho)
        self.camina(unBicho)
        self.atacar(unBicho)

    def atacar(self, unBicho):
        unBicho.atacar()

    def buscarTunelBicho(self, unBicho):
        pass

    def camina(self, unBicho):
        posibles_orientaciones = [ori for ori in unBicho.posicion.obtenerOrientaciones()]
        random.shuffle(posibles_orientaciones)
        for ori in posibles_orientaciones:
            destino = unBicho.posicion.obtenerElementoOr(ori)
            if (hasattr(destino, "esPuerta") and destino.esPuerta() and destino.estaAbierta()) or \
               (hasattr(destino, "esHabitacion") and destino.esHabitacion()):
                ori.caminar(unBicho)

    def dormir(self, unBicho):
        pass

    def esAgresivo(self):
        return False
    
    def esPerezoso(self):
        return False
    
    def __str__(self):
        return "Modo"