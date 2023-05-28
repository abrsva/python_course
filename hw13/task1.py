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
    def __init__(self, sentence: etree.Element):
        self.__sentence = sentence.find('source').text
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
        self.__path_to_corpus = path_to_corpus
        self.__sentences = []

    def load(self):
        tree = etree.parse(self.__path_to_corpus)
        root = tree.getroot()
        for i in root.iter('sentence'):
            sentence2 = Sentence(i)
            self.__sentences.append(sentence2)

    def find_sentence(self, n):
        return self.__sentences[n]


if __name__ == '__main__':
    unittest.main()
