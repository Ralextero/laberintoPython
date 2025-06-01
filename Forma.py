import random


class Forma:

    def __init__(self):
        self.orientaciones = {}

    def agregarOrientacion(self, unaOr):
        self.orientaciones[unaOr.__class__.__name__.lower()] = unaOr

    def irAlEste(self, alguien):
        pass

    def irAlOeste(self, alguien):
        pass

    def irAlNorte(self, alguien):
        pass

    def irAlSur(self, alguien):
        pass

    def obtenerElementoOr(self, unaOr):
        return unaOr.obtenerElementoOrEn(self)
    
    def obtenerOrientacion(self):
        from Norte import Norte
        from Sur import Sur
        from Este import Este
        from Oeste import Oeste
        from Noreste import Noreste
        from Noroeste import Noroeste
        from Sureste import Sureste
        from Suroeste import Suroeste
        orientacion_map = {
            "norte": Norte(),
            "sur": Sur(),
            "este": Este(),
            "oeste": Oeste(),
            "noreste": Noreste(),
            "noroeste": Noroeste(),
            "sureste": Sureste(),
            "suroeste": Suroeste()
        }
        claves_validas = [key.lower() for key in self.orientaciones if key.lower() in orientacion_map]
        if not claves_validas:
            return None
        clave = random.choice(claves_validas)
        return orientacion_map[clave]

    # def obtenerOrientacion(self):
    #     ind = random.randint(0, len(self.orientaciones)-1)
    #     return self.orientaciones[ind]
    
    # def obtenerOrientaciones(self):
    #     return list(self.orientaciones.values())
    
    

    def obtenerOrientaciones(self):
        from Norte import Norte
        from Sur import Sur
        from Este import Este
        from Oeste import Oeste
        from Noreste import Noreste
        from Noroeste import Noroeste
        from Sureste import Sureste
        from Suroeste import Suroeste
        orientacion_map = {
            "norte": Norte(),
            "sur": Sur(),
            "este": Este(),
            "oeste": Oeste(),
            "noreste": Noreste(),
            "noroeste": Noroeste(),
            "sureste": Sureste(),
            "suroeste": Suroeste()
        }
        return [orientacion_map[key.lower()] for key in self.orientaciones if key.lower() in orientacion_map]

    def ponerEnOr(self, unaOr, unEM):
        unaOr.ponerElemento(unEM, self)
    
    def __str__(self):
        return "Forma"
    
    def calcularPosicion(self):
        for or_ in self.orientaciones:
            or_.calcularPosicionDesde(self)

    