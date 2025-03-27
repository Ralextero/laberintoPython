class Modo:

    def __init__(self):
        pass

    def actua(self, unBicho):
        self.dormir(unBicho)
        self.camina(unBicho)
        self.atacar(unBicho)

    def atacar(self, unBicho):
        unBicho.atacar()

    def camina(self, unBicho):
        ori = unBicho.obtenerOrientacion()
        ori.caminar(unBicho)

    def dormir(self, unBicho):
        pass

    def esAgresivo(self):
        return False
    
    def esPerezoso(self):
        return False
    
    def __str__(self):
        return "Modo"