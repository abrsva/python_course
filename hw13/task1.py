import xml.etree.ElementTree as etree
import unittest


class Wordform:
    def __init__(self, grammem):
        self.__word = grammem.attrib['text']
        self.__grammems = []
        for n in grammem.iter('g'):
            self.__grammems.append(n.attrib['v'])

    def find_grammem(self, n):
        return self.__grammems[n]

    def printword(self):
        a = str(self.__word)
        return a


class Sentence:
    def __init__(self, sentence):
        for k in sentence.iter('source'):
            self.__sentence = k.text
        self.__words = []
        for k in sentence.iter('tokens'):
            for j in k.iter('token'):
                w = Wordform(j)
                self.__words.append(w)

    def find_word(self, n):
        return self.__words[n]

    def printsentence(self):
        b = str(self.__sentence)
        return b


class Corpus:

    def __init__(self, path_to_corpus):
        self.path_to_corpus = path_to_corpus
        self.__sentences = []

    def load(self):
        tree = etree.parse(self.path_to_corpus)
        root = tree.getroot()
        for i in root.iter('sentence'):
            sentence2 = Sentence(i)
            self.__sentences.append(sentence2)

    def find_sentence(self, n):
        return self.__sentences[n]


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


if __name__ == '__main__':
    unittest.main()
