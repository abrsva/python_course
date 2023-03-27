import os
import shutil
from unittest import TestCase
from main import write_something


class WriterTest(TestCase):
    def setUp(self):
        self.tests = [("1", None), ("2", ""), ("3", "abcdefg"), ("4", "this is cool test")]
        self.path = r"C:\Users\anna2\PycharmProjects\programming_practice\python_course\hw7\temp"
        for test in self.tests:
            if test[1] is not None:
                write_something(self.path, *test)
            else:
                write_something(self.path, test[0])

    def make_path(self, file):
        return self.path + "/" + file

    def test_exists(self):
        for test in self.tests:
            self.assertTrue(os.path.exists(self.make_path(test[0])))

    def test_content(self):
        for test in self.tests:
            if test[1] is not None:
                with open(self.make_path(test[0]), "r") as f:
                    self.assertEqual(f.read(), test[1])

    def tearDown(self):
        shutil.rmtree(self.path)
