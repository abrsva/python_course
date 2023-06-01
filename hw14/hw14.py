import math
import os
import pickle
import re
from collections import Counter, defaultdict


class TFIDF:

    def __init__(self, directory):
        self.__idf = defaultdict(float)
        self.__directory = directory
        self.__time = 0
        self.__load_instance()

    def __load_instance(self):
        try:
            with open(self.__directory + ".pkl", "rb") as file:
                loaded_object = pickle.load(file)
                if loaded_object.__time != os.path.getmtime(self.__directory):
                    print("Recalculating")
                    self.__calc_instance()
                    return
            self.__time = loaded_object.__time
            self.__idf = loaded_object.__idf
            print("Loaded instance from file")
        except FileNotFoundError:
            self.__calc_instance()

    def __calc_instance(self):
        self.__calc()
        self.__time = os.path.getmtime(self.__directory)
        with open(self.__directory + ".pkl", "wb") as file:
            pickle.dump(self, file)
        print("Calculated")

    def __calc(self):
        files = os.listdir(self.__directory)
        idf_freq = defaultdict(set)
        for file in files:
            tf = TFIDF.calc_tf(self.__directory + "/" + file)
            for word in tf:
                idf_freq[word].add(file)
        for word in idf_freq:
            self.__idf[word] = math.log2(len(files) / len(idf_freq[word]))

    @staticmethod
    def calc_tf(filename):
        tf = defaultdict(float)
        with open(filename, "r", encoding="UTF8") as f:
            words = list(filter(lambda x: len(x) > 0, re.split("[^а-яА-Я]+", f.read().lower())))
            counter = Counter(words)
            for word in counter:
                tf[word] = counter[word] / len(words)
        return tf

    def calc_tf_idf(self, filename):
        return [(word, value * self.__idf[word]) for word, value in TFIDF.calc_tf(filename).items()]

    def get_idf(self):
        return self.__idf.copy()

    def get_time(self):
        return self.__time
