import unittest
import os
from converter.file_handler import read_file, save_results

class TestFileHandler(unittest.TestCase):
    def setUp(self):
        # Створення тимчасових файлів для тестів
        self.input_file = "test_input.txt"
        self.output_file = "test_output.txt"
        with open(self.input_file, "w") as file:
            file.write("1010")

    def tearDown(self):
        # Видалення тимчасових файлів після тестів
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_read_file(self):
        content = read_file(self.input_file)
        self.assertEqual(content, "1010")

    def test_save_results(self):
        results = {
            "Двійкова": "1010",
            "Вісімкова": "12",
            "Десяткова": "10",
            "Шістнадцяткова": "A"
        }
        save_results(self.output_file, results)

        with open(self.output_file, "r") as file:
            content = file.read()

        expected_content = (
            "Результати конвертації:\n"
            "Двійкова: 1010\n"
            "Вісімкова: 12\n"
            "Десяткова: 10\n"
            "Шістнадцяткова: A\n"
        )
        self.assertEqual(content, expected_content)

if __name__ == "__main__":
    unittest.main()
