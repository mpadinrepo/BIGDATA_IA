
class TestCalcularAreaCirculo(unittest.TestCase):

    def test_area_circulo_radio_cero(self):
        self.assertEqual(calcular_area_circulo(0), 0)

    def test_area_circulo_radio_uno(self):
        self.assertAlmostEqual(calcular_area_circulo(1), math.pi)

    def test_area_circulo_radio_dos(self):
        self.assertAlmostEqual(calcular_area_circulo(2), 4 * math.pi)

class TestCalcularVolumenCilindro(unittest.TestCase):

    def test_volumen_cilindro_radio_cero_altura_uno(self):
        self.assertEqual(calcular_volumen_cilindro(0, 1), 0)

    def test_volumen_cilindro_radio_uno_altura_uno(self):
        self.assertAlmostEqual(calcular_volumen_cilindro(1, 1), math.pi)

    def test_volumen_cilindro_radio_dos_altura_dos(self):
        self.assertAlmostEqual(calcular_volumen_cilindro(2, 2), 8 * math.pi)

if __name__ == "__main__":
    unittest.main()