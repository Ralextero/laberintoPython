from unittest import TestCase
from Cofre import Cofre
from Habitacion import Habitacion
from Llave import Llave
from Moneda import Moneda
from Personaje import Personaje

class ObjetosSimplesTest(TestCase):
    def setUp(self):
        self.personaje = Personaje("TestHero")

    def test_llave(self):
        llave = Llave()
        hab = Habitacion()
        self.personaje.posicion = hab
        hab.agregarHijo(llave)
        llave.interactuar(self.personaje)
        self.assertTrue(self.personaje.mochila.tieneLlave())

    def test_moneda(self):
        moneda = Moneda()
        hab = Habitacion()
        self.personaje.posicion = hab
        hab.agregarHijo(moneda)
        moneda.interactuar(self.personaje)
        self.assertEqual(self.personaje.mochila.contarMonedas(), 1)

    def test_cofre(self):
        from Casco import Casco
        from Pechera import Pechera
        from Pantalones import Pantalones
        from Botas import Botas
        from Espada import Espada
        from Moneda import Moneda
        posibles_objetos = [Casco, Pechera, Pantalones, Botas, Espada, Moneda]
        cofre = Cofre(posibles_objetos)
        self.assertTrue(cofre.esCofre())
        self.assertTrue(len(cofre.hijos) == 3)
        # Recoger un objeto del cofre
        obj = cofre.hijos[0]
        cofre.recoger_objeto(self.personaje, 0)
        self.assertNotIn(obj, cofre.hijos)