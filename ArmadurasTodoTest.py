from unittest import TestCase
from Bicho import Bicho
from Cabeza import Cabeza
from Habitacion import Habitacion
from Personaje import Personaje
from Casco import Casco
from Pechera import Pechera
from Pantalones import Pantalones
from Botas import Botas
from Diamante import Diamante
from Hierro import Hierro
from Oro import Oro
from Manos import Manos
from Piernas import Piernas
from Pies import Pies
from Tronco import Tronco

class ArmaduraMaterialTest(TestCase):
    def setUp(self):
        self.personaje = Personaje("TestHero")

    def test_equipar_armaduras(self):
        casco = Casco(Cabeza(), Diamante())
        pechera = Pechera(Tronco(), Hierro())
        pantalones = Pantalones(Piernas(), Oro())
        botas = Botas(Pies(), Hierro())
        self.personaje.equipar(casco)
        self.personaje.equipar(pechera)
        self.personaje.equipar(pantalones)
        self.personaje.equipar(botas)
        # Comprobar que están equipadas
        self.assertIs(self.personaje.cabeza, casco)
        self.assertIs(self.personaje.tronco, pechera)
        self.assertIs(self.personaje.piernas, pantalones)
        self.assertIs(self.personaje.pies, botas)

    def test_bonificaciones(self):
        casco = Casco(Cabeza(), Diamante())
        self.personaje.equipar(casco)
        self.assertEqual(self.personaje.defensa_total(), casco.bonificacion_defensa())
        bicho = Bicho()
        bicho.poder = 50
        pos = Habitacion()
        pos.num = 1
        bicho.posicion = pos
        self.personaje.posicion = pos
        vidas_antes = self.personaje.vidas
        self.personaje.esAtacadoPor(bicho)
        self.assertEqual(self.personaje.vidas, vidas_antes - (bicho.poder - self.personaje.defensa_total()))