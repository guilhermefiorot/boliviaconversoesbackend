import os
import sys
import unittest

# Adicionar o diretório src ao path ANTES de importar
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.roman_converter import int_to_roman


class TestConversaoNumerosRomanos(unittest.TestCase):
    def test_numeros_basicos(self):
        """Testa conversão de números básicos"""
        self.assertEqual(int_to_roman(1), "I")
        self.assertEqual(int_to_roman(4), "IV")
        self.assertEqual(int_to_roman(5), "V")
        self.assertEqual(int_to_roman(9), "IX")
        self.assertEqual(int_to_roman(10), "X")
        self.assertEqual(int_to_roman(40), "XL")
        self.assertEqual(int_to_roman(50), "L")
        self.assertEqual(int_to_roman(90), "XC")
        self.assertEqual(int_to_roman(100), "C")
        self.assertEqual(int_to_roman(400), "CD")
        self.assertEqual(int_to_roman(500), "D")
        self.assertEqual(int_to_roman(900), "CM")
        self.assertEqual(int_to_roman(1000), "M")

    def test_numeros_compostos(self):
        """Testa conversão de números mais complexos"""
        self.assertEqual(int_to_roman(14), "XIV")
        self.assertEqual(int_to_roman(49), "XLIX")
        self.assertEqual(int_to_roman(99), "XCIX")
        self.assertEqual(int_to_roman(500), "D")
        self.assertEqual(int_to_roman(2023), "MMXXIII")
        self.assertEqual(int_to_roman(3888), "MMMDCCCLXXXVIII")

    def test_casos_limite(self):
        """Testa os limites de conversão"""
        self.assertEqual(int_to_roman(1), "I")
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")

    def test_entrada_invalida(self):
        """Testa entradas inválidas"""
        with self.assertRaises(TypeError):
            int_to_roman("10")

        with self.assertRaises(ValueError):
            int_to_roman(0)

        with self.assertRaises(ValueError):
            int_to_roman(4000)


if __name__ == "__main__":
    unittest.main()
