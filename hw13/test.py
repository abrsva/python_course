import unittest

from task1 import Corpus


class Test(unittest.TestCase):

    def setUp(self):
        self.corpustest = Corpus('annot.opcorpora.no_ambig.xml')
        self.corpustest.load()

    def test_sentence(self):
        self.assertTrue(self.corpustest.find_sentence(
            5).printsentence() == "В остальном «Школа злословия» представляла собой интервью ведущих с героем выпуска.")

    def test_word(self):
        self.assertTrue(self.corpustest.find_sentence(5).find_word(1).find_grammem(0) == 'ADJF')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(1).find_grammem(1) == 'Subx')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(1).find_grammem(2) == 'Apro')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(1).find_grammem(3) == 'neut')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(1).find_grammem(4) == 'sing')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(1).find_grammem(5) == 'loct')

    def test_grammem(self):
        self.assertTrue(self.corpustest.find_sentence(5).find_word(0).printword() == 'В')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(1).printword() == 'остальном')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(2).printword() == '«')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(3).printword() == 'Школа')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(4).printword() == 'злословия')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(5).printword() == '»')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(6).printword() == 'представляла')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(7).printword() == 'собой')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(8).printword() == 'интервью')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(9).printword() == 'ведущих')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(10).printword() == 'с')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(11).printword() == 'героем')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(12).printword() == 'выпуска')
        self.assertTrue(self.corpustest.find_sentence(5).find_word(13).printword() == '.')
