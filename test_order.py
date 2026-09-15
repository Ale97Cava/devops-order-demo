
import unittest
from order import totale


class TestOrder(unittest.TestCase):

    def test_calcola_totale(self):
        risultato = totale(10, 4)
        self.assertEqual(risultato, 40)


if __name__ == "__main__":
    unittest.main()