import unittest
from nlp071 import StopList

class TestStopList(unittest.TestCase):
    def setUp(self):
        obj = StopList()
        self.obj = obj

    def test_is_in_stoplist(self):
        self.obj.set_stoplist(["the"])
        self.assertEqual(True, self.obj.in_stoplist("the"))

    def test_return_false_when_a_word_not_in_stoplist(self):
        self.obj.set_stoplist(["the"])
        self.assertEqual(False, self.obj.in_stoplist("for"))

if __name__ == '__main__':
    unittest.main()
