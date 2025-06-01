from unittest import TestCase
from LaberintoBuilderOctogono import LaberintoBuilderOctogono
from Habitacion import Habitacion

class OctogonoTest(TestCase):
    def setUp(self):
        self.builder = LaberintoBuilderOctogono()
        self.hab = Habitacion()
        self.hab.forma = self.builder.fabricarForma()

    def test_orientaciones(self):
        orientaciones = self.hab.obtenerOrientaciones()
        self.assertEqual(len(orientaciones), 8)
        nombres = [str(or_) for or_ in orientaciones]
        for esperado in ["Norte", "Noreste", "Este", "Sureste", "Sur", "Suroeste", "Oeste", "Noroeste"]:
            self.assertIn(esperado, nombres)