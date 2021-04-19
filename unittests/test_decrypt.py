import unittest
from utils import utils

class test_decrypt(unittest.TestCase):

    #test the decrypt() method
    def test_decrypt(self):
        #decrypt letters only
        a = utils.decrypt("qbpq")
        self.assertEqual(a, "test")

        #decrypt numbers only
        b = utils.decrypt("8765")
        self.assertEqual(b, "1234")

        #decrypt letters and numbers
        c = utils.decrypt("qbpq8765")
        self.assertEqual(c, "test1234")

        #decrypt non-alphanumeric characters only
        d = utils.decrypt("!£$%")
        self.assertEqual(d, "!£$%")

        #decrypt letters and non-alphanumeric characters
        e = utils.decrypt("qbpq!£$%")
        self.assertEqual(e, "test!£$%")

        #decrypt numbers and non-alphanumeric characters
        f = utils.decrypt("8765!£$%")
        self.assertEqual(f, "1234!£$%")

        #decrypt alphanumeric and non-alphanumeric characters
        g = utils.decrypt("qbpq8765!£$%")
        self.assertEqual(g, "test1234!£$%")