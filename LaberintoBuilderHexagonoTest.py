from unittest import TestCase
from LaberintoBuilderHexagono import LaberintoBuilderHexagono
from Habitacion import Habitacion

class HexagonoTest(TestCase):
    def setUp(self):
        self.builder = LaberintoBuilderHexagono()
        self.hab = Habitacion()
        self.hab.forma = self.builder.fabricarForma()

    def test_orientaciones(self):
        orientaciones = self.hab.obtenerOrientaciones()
        self.assertEqual(len(orientaciones), 6)
        nombres = [str(or_) for or_ in orientaciones]
        for esperado in ["Norte", "Noreste", "Sureste", "Sur", "Suroeste", "Noroeste"]:
            self.assertIn(esperado, nombres)