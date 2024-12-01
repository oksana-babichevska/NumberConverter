import unittest
from converter.core import convert_to_binary, convert_to_octal, convert_to_decimal, convert_to_hexadecimal

class TestCoreFunctions(unittest.TestCase):
    def test_convert_to_binary(self):
        self.assertEqual(convert_to_binary(10), "1010")
        self.assertEqual(convert_to_binary(255), "11111111")
        self.assertEqual(convert_to_binary(0), "0")

    def test_convert_to_octal(self):
        self.assertEqual(convert_to_octal(10), "12")
        self.assertEqual(convert_to_octal(255), "377")
        self.assertEqual(convert_to_octal(0), "0")

    def test_convert_to_decimal(self):
        self.assertEqual(convert_to_decimal("1010", 2), 10)
        self.assertEqual(convert_to_decimal("377", 8), 255)
        self.assertEqual(convert_to_decimal("FF", 16), 255)

    def test_convert_to_hexadecimal(self):
        self.assertEqual(convert_to_hexadecimal(10), "A")
        self.assertEqual(convert_to_hexadecimal(255), "FF")
        self.assertEqual(convert_to_hexadecimal(0), "0")

if __name__ == "__main__":
    unittest.main()
