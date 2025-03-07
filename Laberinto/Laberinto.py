from abc import ABC, abstractmethod
from FactoryMethod.FactoryMethod import Creator

class ElementoMapa:

    def entrar(self):
        pass

    def entrar(self, alguien):
        pass

    def esBomba(self):
        pass

    def esHabitacion(self):
        pass

    def esLaberinto(self):
        pass

    def esPared(self):
        pass

    def esPuerta(self):
        pass

    def get_padre(self):
        return self.padre
    
    def set_padre(self, padre):
        self.padre = padre


class Contenedor(ElementoMapa):

    def __init__(self):
        self.hijos = []
        self.orientaciones = []

    def agregarHijo(self, unEM):
        unEM.set_padre(self)
        self.hijos.append(unEM)

    def agregarOrientacion(self, unaOrientacion):
        self.orientaciones.append(unaOrientacion)

    def eliminarHijo(self, unEM):
        try:
            self.hijos.remove(unEM)

        except ValueError:
            print("No existe ese objeto hijo")

    def get_hijos(self):
        return self.hijos
    
    def set_hijos(self, hijos):
        self.hijos = hijos

    def get_orientaciones(self):
        return self.orientaciones
    
    def set_orientaciones(self, orientaciones):
        self.orientaciones = orientaciones

    def obtenerElementoOr(self, unaOrientacion):
        return unaOrientacion.ObtenerElementoOrEn(self)
    
    def ponerEnOr(self, unEM, unaOrientacion):
        unaOrientacion.ponerElemento(unEM, self)
    

class Habitacion(Contenedor):

    def entrar(self):
        return "Estas en una habitacion"
    
    def esHabitacion(self):
        return True
    
    def get_este(self):
        return self.este
    
    def set_este(self, este):
        self.este = este

    def get_norte(self):
        return self.norte
    
    def set_norte(self, norte):
        self.norte = norte

    def get_oeste(self):
        return self.oeste
    
    def set_oeste(self, oeste):
        self.oeste = oeste

    def get_sur(self):
        return self.sur
    
    def set_sur(self, sur):
        self.sur = sur

    def get_num(self):
        return self.num
    
    def set_num(self, num):
        self.num = num

class Laberinto(Contenedor):

    def entrar(self):
        return "Estas en un laberinto"
    
    def esLaberinto(self):
        return True
    
    def agregarHabitacion(self, unaHabitacion):
        self.hijos.append(unaHabitacion)

    def eliminarHabitacion(self, unaHabitacion):
        try:
            self.hijos.remove(unaHabitacion)

        except ValueError:
            print("No existe ese objeto habitacion")

    def obtenerHabitacion(self, num):
        for habitacion in self.hijos:
            if habitacion.get_num() == num:
                return habitacion
        return None
            
class Orientacion:

    def ponerElemento(self, unEM, unContenedor):
        pass

    def ObtenerElementoOrEn(self, unContenedor):
        pass

class Norte(Orientacion):

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.norte = unEM

    def ObtenerElementoOrEn(self, unContenedor):
        return unContenedor.norte
    
class Sur(Orientacion):
    
    def ponerElemento(self, unEM, unContenedor):
        unContenedor.sur = unEM

    def ObtenerElementoOrEn(self, unContenedor):
        return unContenedor.sur
    
class Este(Orientacion):
    
    def ponerElemento(self, unEM, unContenedor):
        unContenedor.este = unEM

    def ObtenerElementoOrEn(self, unContenedor):
        return unContenedor.este
    
class Oeste(Orientacion):
    
    def ponerElemento(self, unEM, unContenedor):
        unContenedor.oeste = unEM

    def ObtenerElementoOrEn(self, unContenedor):
        return unContenedor.oeste
    
class Modo:

    def actua(self, unBicho):
        self.camina(unBicho)

    #def camina(self, unBicho):
        #por hacer

    def esAgresivo(self):
        return False
    
    def esPerezoso(self):
        return False

class Agresivo(Modo):

    def __init__(self):
        super().__init__()

    def esAgresivo(self):
        return True

class Perezoso(Modo):
    
    def __init__(self):
        super().__init__()

    def esPerezoso(self):
        return True

class Hoja:
    pass

class Decorator(Hoja):

    def get_em(self):
        return self.em
    
    def set_em(self, em):
        self.em = em

class Bomba(Decorator):
    
    def get_activa(self):
        return self.activa
    
    def set_activa(self, activa):
        self.activa = activa

    def entrar(self):
        if self.activa:
            return "Te metiste una bomba en la cara"
        else:
            return "Estas en una bomba"

    def esBomba(self):
        return True

    def __init__(self):
        self.activa = False

class Pared(Decorator):
    
    def entrar(self):
        return "Te has chocado con una pared"

    def esPared(self):
        return True

class ParedBomba(Pared):

    def entrar(self):
        return "Te has chocado con una pared con bomba"

    def __init__(self):
        self.activa = False

    def get_activa(self):
        return self.activa

    def set_activa(self, activa):
        self.activa = activa

class Puerta(Decorator):

    def get_abierta(self):
        return self.abierta

    def set_abierta(self, abierta):
        self.abierta = abierta

    def entrar(self):
        if self.abierta:
            return "Has pasado por una puerta"
        else:
            return "Te has chocado con una puerta"

    def esPuerta(self):
        return True

    def __init__(self):
        self.abierta = False

    def get_lado1(self):
        return self.lado1

    def set_lado1(self, lado1):
        self.lado1 = lado1

    def get_lado2(self):
        return self.lado2

    def set_lado2(self, lado2):
        self.lado2 = lado2

class Bicho:

    def __init__(self):
        self.vidas = 5
        self.poder = 1

    def actua(self):
        self.modo.actua(self)

    def esAgresivo(self):
        return self.modo.esAgresivo()

    def esPerezoso(self):
        return self.modo.esPerezoso()

    def iniAgresivo(self):
        self.modo = Agresivo()

    def iniPerezoso(self):
        self.modo = Perezoso()

    def get_modo(self):
        return self.modo

    def set_modo(self, modo):
        self.modo = modo

    def get_poder(self):
        return self.poder

    def set_poder(self, poder): 
        self.poder = poder

    def get_vidas(self):
        return self.vidas

    def set_vidas(self, vidas):
        self.vidas = vidas

    def get_posicion(self):
        return self.posicion

    def set_posicion(self, posicion):
        self.posicion = posicion

class Juego:

    def agregarBicho(self, unBicho):
        self.bichos.append(unBicho)

    def get_bichos(self):
        return self.bichos

    def set_bichos(self, bichos):
        self.bichos = bichos

    def crearLaberinto2Habitaciones(self):

        hab1 = Habitacion()
        hab1.set_num(1)
        hab1.set_este(Pared())
        hab1.set_norte(Pared())
        hab1.set_oeste(Pared())

        hab2 = Habitacion()
        hab2.set_num(2)
        hab2.set_sur(Pared())
        hab2.set_oeste(Pared())
        hab2.set_este(Pared())

        puerta = Puerta()
        puerta.set_lado1(hab1)
        puerta.set_lado2(hab2)

        hab1.set_sur(puerta)
        hab2.set_norte(puerta)

        laberinto = Laberinto()
        laberinto.agregarHabitacion(hab1)
        laberinto.agregarHabitacion(hab2)
        return laberinto

    def crearLaberinto2HabitacionesFM(self):

        unFM = Creator()

        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)

        puerta = unFM.fabricarPuerta()
        puerta.set_lado1(hab1)
        puerta.set_lado2(hab2)

        hab1.set_sur(puerta)
        hab2.set_norte(puerta)

        laberinto = unFM.fabricarLaberinto()
        laberinto.agregarHabitacion(hab1)
        laberinto.agregarHabitacion(hab2)

        return laberinto
    
    def crearLaberinto2HabitacionesFM(self, unFM):
        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)

        puerta = unFM.fabricarPuerta()

        puerta.set_lado1(hab1)
        puerta.set_lado2(hab2)

        hab1.ponerEnOr(puerta, unFM.fabricarSur())
        hab2.ponerEnOr(puerta, unFM.fabricarNorte())    

        laberinto = unFM.fabricarLaberinto()
        laberinto.agregarHabitacion(hab1)
        laberinto.agregarHabitacion(hab2)

        return laberinto
    
    def crearLaberinto2HabitacionesFMD(self, unFM):
        
        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)

        bomba1 = unFM.fabricarBomba()
        bomba1.em = unFM.fabricarPared()
        hab1.set_este=bomba1

        bomba2 = unFM.fabricarBomba()
        bomba2.em = unFM.fabricarPared()
        hab2.set_este=bomba2

        puerta = unFM.fabricarPuerta()
        puerta.set_lado1(hab1)
        puerta.set_lado2(hab2)

        hab1.set_sur(puerta)
        hab2.set_norte(puerta)

        laberinto = unFM.fabricarLaberinto()
        laberinto.agregarHabitacion(hab1)
        laberinto.agregarHabitacion(hab2)

        return laberinto
    
    def crearLaberinto4H4BFM(self,unFM):

        norte = unFM.fabricarNorte()
        sur = unFM.fabricarSur()
        este = unFM.fabricarEste()
        oeste = unFM.fabricarOeste()


        hab1 = unFM.fabricarHabitacion(1)
        hab2 = unFM.fabricarHabitacion(2)
        hab3 = unFM.fabricarHabitacion(3)
        hab4 = unFM.fabricarHabitacion(4)

        puerta1 = unFM.fabricarPuerta()
        puerta2 = unFM.fabricarPuerta()
        puerta3 = unFM.fabricarPuerta()
        puerta4 = unFM.fabricarPuerta()

        puerta1.set_lado1(hab1)
        puerta1.set_lado2(hab2)
        puerta2.set_lado1(hab1)
        puerta2.set_lado2(hab3)
        puerta3.set_lado1(hab2)
        puerta3.set_lado2(hab4)
        puerta4.set_lado1(hab3)
        puerta4.set_lado2(hab4)

        hab1.ponerEnOr(puerta1, sur)
        hab2.ponerEnOr(puerta1, norte)
        hab1.ponerEnOr(puerta2, este)
        hab3.ponerEnOr(puerta2, oeste)
        hab2.ponerEnOr(puerta3, este)
        hab4.ponerEnOr(puerta3, oeste)
        hab3.ponerEnOr(puerta4, sur)
        hab4.ponerEnOr(puerta4, norte)

        bicho1 = unFM.fabricarBichoAgresivo()
        bicho2 = unFM.fabricarBichoAgresivo()
        bicho3 = unFM.fabricarBichoPerezoso()
        bicho4 = unFM.fabricarBichoPerezoso()

        laberinto = unFM.fabricarLaberinto()
        laberinto.agregarHabitacion(hab1)
        laberinto.agregarHabitacion(hab2)
        laberinto.agregarHabitacion(hab3)
        laberinto.agregarHabitacion(hab4)
        laberinto.agregarBicho(bicho1)
        laberinto.agregarBicho(bicho2)
        laberinto.agregarBicho(bicho3)
        laberinto.agregarBicho(bicho4)

        bicho1.set_posicion(hab1)
        bicho2.set_posicion(hab3)
        bicho3.set_posicion(hab2)
        bicho4.set_posicion(hab4)

        return laberinto
    
    def eliminarBichos(self, unBicho):
        try:
            self.bichos.remove(unBicho)

        except ValueError:
            print("No existe ese objeto bicho")


    def __init__(self):
        self.bichos = []

    
    def get_laberinto(self):
        return self.laberinto
    
    def set_laberinto(self, laberinto):
        self.laberinto = laberinto

    def obtenerHabitacion(self, num):
        return self.laberinto.obtenerHabitacion(num)