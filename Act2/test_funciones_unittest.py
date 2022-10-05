import unittest
import funciones

class Test_Funciones(unittest.TestCase):
    def setUp(self):
        print ("Entrando en setUp")
    
    def tearDown(self):
        print ("Entrando en tearDown")

    def test_suma(self):
        self.assertEqual(funciones.sumar(21,5), 26)

    def test_resta(self):
        self.assertEqual(funciones.restar(21,5), 16)

    def test_multiplicacion(self):
        self.assertEqual(funciones.multiplicar(15,3), 45)

    def test_división(self):
        self.assertEqual(funciones.dividir(45,3), 15)
    
    def test_factorial(self):
        self.assertEqual(funciones.factorial(5), 120)

    def test_acirculo(self):
        self.assertEqual(funciones.area_circulo(2),12.566)
    
    def test_acuadrado(self):
        self.assertEqual(funciones.area_cuadrado(5),25)

    def test_atriangulo(self):
        self.assertEqual(funciones.area_triangulo(4,3),6)

    def test_arectangulo(self):
        self.assertEqual(funciones.area_rectangulo(20,12),240)
    

