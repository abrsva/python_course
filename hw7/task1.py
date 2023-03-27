from unittest import TestCase
from main import *


class SimpleTests(TestCase):
    def test_subtract(self):
        for x in range(-10, 100, 2):
            for y in range(-100, 100, 25):
                res = subtract(x, y)
                self.assertEqual(res, x - y)
                if x >= y:
                    self.assertGreaterEqual(res, 0)
                else:
                    self.assertLess(res, 0)

    def test_unique_ascending(self):
        tests = [
            [1, 1, 2, 3, 1, 2],
            [5, 3, 4, 1, 2, 3],
            [1000, 241, 1, 241, 2],
            [100, 100, 100, 100, 100]
        ]
        for test in tests:
            res = unique_ascending(test)
            # Проверка, что он действительно в порядке неубывания
            for i in range(len(res) - 1):
                self.assertGreaterEqual(res[i + 1], res[i])
            # Проверка, что в результирующем списке действительно все элементы из исходного
            for x in test:
                self.assertIn(x, res)
