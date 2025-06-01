from unittest import TestCase
from PuertaConLlave import PuertaConLlave
from Habitacion import Habitacion
from Personaje import Personaje
from Llave import Llave

class PuertaConLlaveTest(TestCase):
    def setUp(self):
        self.hab1 = Habitacion()
        self.hab2 = Habitacion()
        self.puerta = PuertaConLlave()
        self.puerta.lado1 = self.hab1
        self.puerta.lado2 = self.hab2
        self.personaje = Personaje("TestHero")

    def test_no_se_abre_sin_llave(self):
        self.personaje.mochila.vaciar()
        self.assertFalse(self.personaje.mochila.tieneLlave())
        self.puerta.abrir(self.personaje)
        self.assertFalse(self.puerta.estaAbierta())

    def test_se_abre_con_llave(self):
        llave = Llave()
        self.personaje.mochila.agregar(llave)
        self.puerta.abrir(self.personaje)
        self.assertTrue(self.puerta.estaAbierta())