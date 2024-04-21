import unittest
from io import StringIO
from unittest.mock import patch
import taschenrechner_musterloesung as taschenrechner


class TestTaschenrechner(unittest.TestCase):

    def test_addieren(self):
        self.assertEqual(taschenrechner.addieren(5, 3), 8)

    def test_subtrahieren(self):
        self.assertEqual(taschenrechner.subtrahieren(5, 3), 2)

    def test_multiplizieren(self):
        self.assertEqual(taschenrechner.multiplizieren(5, 3), 15)

    def test_dividieren(self):
        self.assertEqual(taschenrechner.dividieren(10, 2), 5)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=["2", "2", "1", "0"])
    def test_main_output_enthält_ergebnis(self, mock_input, mock_stdout):
        with patch('taschenrechner.get_float'), patch('taschenrechner.get_int'):
            taschenrechner.main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Ergebnis: 4.0", output)

    @patch('builtins.input', side_effect=["3.5"])
    def test_zahl_abfragen(self, mock_input):
        result = taschenrechner.zahl_abfragen()
        self.assertEqual(result, 3.5)

    @patch('builtins.input', side_effect=["2"])
    def test_matheoperation_abfragen(self, mock_input):
        result = taschenrechner.rechenart_abfragen()
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=["5", "a", "3"])
    def test_matheoperation_abfragen_falsche_eingabe(self, mock_input):
        result = taschenrechner.rechenart_abfragen()
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
