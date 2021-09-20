from main import Main
import unittest


class TestMain(unittest.TestCase):
    def setUp(self):
        self.main = Main()


class TestIndexOf(TestMain):
    def test_index_of_1(self):
        self.assertEqual(self.main.index_of("testcase", "test"), 0)

    def test_index_of_2(self):
        self.assertEqual(self.main.index_of("01234testcase", "test"), 5)

    def test_index_of_3(self):
        self.assertEqual(self.main.index_of("Mississippi", "sip"), 6)

    def test_index_of_4(self):
        self.assertEqual(self.main.index_of("012345tetcase", "test"), -1)


class TestSquareRoot(Main):
    def test_square_root_guess_1(self):
        assert True
