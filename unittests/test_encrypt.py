import unittest
from utils import utils

class test_encrypt(unittest.TestCase):

    #test the encrypt() method 
    def test_encrypt(self):
        #encrypt letters only
        a = utils.encrypt("test")
        self.assertEqual(a, "qbpq")

        #encrypt numbers only
        b = utils.encrypt("1234")
        self.assertEqual(b, "8765")

        #encypt letters and numbers
        c = utils.encrypt("test1234")
        self.assertEqual(c, "qbpq8765")

        #encrypt non-alphanumeric characters only
        d = utils.encrypt("!£$%")
        self.assertEqual(d, "!£$%")

        #encrypt letters and non-alphanumeric characters
        e = utils.encrypt("test!£$%")
        self.assertEqual(e, "qbpq!£$%")

        #encrypt numbers and non-alphanumeric characters
        f = utils.encrypt("1234!£$%")
        self.assertEqual(f, "8765!£$%")

        #encrypt alphanumeric and non-alphanumeric characters
        g = utils.encrypt("test1234!£$%")
        self.assertEqual(g, "qbpq8765!£$%")