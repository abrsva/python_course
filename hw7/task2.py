from unittest import TestCase
from random import randint
from main import *


class HardTests(TestCase):
    def test_subtract(self):
        for x in (randint(-1000, 1000) for _ in range(100)):
            for y in (randint(-1000, 1000) for _ in range(100)):
                with self.subTest(x=x, y=y):
                    res = subtract(x, y)
                    self.assertEqual(res, x - y)
                    if x >= y:
                        self.assertGreaterEqual(res, 0)
                    else:
                        self.assertLess(res, 0)

    def test_unique_ascending(self):
        for test in ([randint(-20, 20) for _ in range(randint(1, 200))] for _ in range(10000)):
            with self.subTest(test=test):
                res = unique_ascending(test)
                # Проверка, что он действительно в порядке неубывания
                for i in range(len(res) - 1):
                    self.assertGreaterEqual(res[i + 1], res[i])
                # Проверка, что в результирующем списке действительно все элементы из исходного
                for x in test:
                    self.assertIn(x, res)
