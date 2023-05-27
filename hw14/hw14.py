import math
import os
import pickle
import re
from collections import Counter, defaultdict


class TFIDF:

    def __init__(self, directory):
        self.idf = defaultdict(float)
        self.directory = directory
        self.time = 0
        self.__load_instance()

    def __load_instance(self):
        try:
            with open(self.directory + ".pkl", "rb") as file:
                loaded_object = pickle.load(file)
                if loaded_object.time != os.path.getmtime(self.directory):
                    print("Recalculating")
                    self.__calc_instance()
                    return
            self.time = loaded_object.time
            self.idf = loaded_object.idf
            print("Loaded instance from file")
        except FileNotFoundError:
            self.__calc_instance()

    def __calc_instance(self):
        self.__calc()
        self.time = os.path.getmtime(self.directory)
        with open(self.directory + ".pkl", "wb") as file:
            pickle.dump(self, file)
        print("Calculated")

    def __calc(self):
        files = os.listdir(self.directory)
        idf_freq = defaultdict(set)
        for file in files:
            tf = TFIDF.calc_tf(self.directory + "/" + file)
            for word in tf:
                idf_freq[word].add(file)
        for word in idf_freq:
            self.idf[word] = math.log2(len(files) / len(idf_freq[word]))

    @classmethod
    def calc_tf(cls, filename):
        tf = defaultdict(float)
        with open(filename, "r", encoding="UTF8") as f:
            words = list(filter(lambda x: len(x) > 0, re.split("[^а-яА-Я]+", f.read().lower())))
            counter = Counter(words)
            for word in counter:
                tf[word] = counter[word] / len(words)
        return tf

    def calc_tf_idf(self, filename):
        return [(word, value * self.idf[word]) for word, value in TFIDF.calc_tf(filename).items()]
