import os
import unittest

from hw14 import TFIDF


class Tests(unittest.TestCase):

    def setUp(self):
        self.tfidf = TFIDF("test")

    def test_tf(self):
        tf = TFIDF.calc_tf("test.txt")
        self.assertAlmostEqual(tf["заплачу"], 2 / 5)
        self.assertAlmostEqual(tf["глупенькая"], 1 / 5)
        self.assertAlmostEqual(tf["женщины"], 1 / 5)
        self.assertAlmostEqual(tf["кто"], 1 / 5)

    def test_idf(self):
        self.assertEqual(self.tfidf._time, os.path.getmtime("test"))
        idf = self.tfidf.get_idf()
        self.assertEqual(len(set(idf.values())), len(os.listdir("test")))
        self.assertAlmostEqual(idf["заплачу"], 2.321928094887362)
        self.assertAlmostEqual(idf["глупенькая"], 2.321928094887362)
        self.assertAlmostEqual(idf["кольцо"], 1.3219280948873624)
        self.assertAlmostEqual(idf["женщины"], 1.3219280948873624)
        self.assertAlmostEqual(idf["кто"], 0.7369655941662062)
        self.assertAlmostEqual(idf["с"], 0.32192809488736235)

    def test_tf_idf(self):
        tfidf = self.tfidf.calc_tf_idf("test.txt")
        results = {'заплачу': 0.9287712379549449,
                   'женщины': 0.2643856189774725,
                   'глупенькая': 0.46438561897747244,
                   'кто': 0.14739311883324124}
        for word, value in tfidf:
            self.assertAlmostEqual(value, results[word])
