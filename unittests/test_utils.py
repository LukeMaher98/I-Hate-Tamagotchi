import unittest
from utils import utils

class test_utils(unittest.TestCase):

    def test_convertToDisplayForm(self):
        #correct input
        a = utils.convertToDisplayForm("FilmName,1,01:00,02:00")
        self.assertEqual(a, "Screen 1 -  FilmName:  01:00 02:00 ")

        #one incorrect time
        b = utils.convertToDisplayForm("FilmName,1,01:a0,02:00")
        self.assertEqual(b, "Screen 1 -  FilmName:  02:00 ")

        #two incorrect times
        c = utils.convertToDisplayForm("FilmName,1,01:a0,02:a0")
        self.assertEqual(c, "Screen 1 -  FilmName:  ")

        #incorrect screen 
        d = utils.convertToDisplayForm("FilmName,a,01:00,02:00")
        self.assertEqual(d, "01:00 02:00 ")

        #no times
        e = utils.convertToDisplayForm("FilmName,1")
        self.assertEqual(e, "Screen 1 -  FilmName:  ")

        #no screen or times
        f = utils.convertToDisplayForm("FilmName")
        self.assertEqual(f, "")

    def test_convertToEditForm(self):
        #correct input
        a = utils.convertToEditForm("Screen 1 -  FilmName:  01:00 02:00 ")
        self.assertEqual(a, "FilmName,1,01:00,02:00")

        #one incorrect time
        b = utils.convertToEditForm("Screen 1 -  FilmName:  01:a0 02:00 ")
        self.assertEqual(b, "FilmName,1,01:a0,02:00")

        #two incorrect time
        c = utils.convertToEditForm("Screen 1 -  FilmName:  01:a0 02:a0 ")
        self.assertEqual(c, "FilmName,1,01:a0,02:a0")

        #incorrect screen
        d = utils.convertToEditForm("Screen a -  FilmName:  01:00 02:00 ")
        self.assertEqual(d, "FilmName,a,01:00,02:00")

        #no times
        e = utils.convertToEditForm("Screen 1 -  FilmName:  ")
        self.assertEqual(e, "FilmName,1")

        #no filename or times
        e = utils.convertToEditForm("Screen 1 -  ")
        self.assertEqual(e, ",1")

    def test_convertToSaveForm(self):
        #correct input
        a = utils.convertToSaveForm("Screen 1 -  FilmName:  01:00 02:00 ")
        self.assertEqual(a, "FilmName,1, 01:00, 02:00, ")

        #one incorrect time
        b = utils.convertToSaveForm("Screen 1 -  FilmName:  01:a0 02:00 ")
        self.assertEqual(b, "FilmName,1, 01:a0, 02:00, ")

        #two incorrect time
        c = utils.convertToSaveForm("Screen 1 -  FilmName:  01:a0 02:a0 ")
        self.assertEqual(c, "FilmName,1, 01:a0, 02:a0, ")

        #incorrect screen
        d = utils.convertToSaveForm("Screen a -  FilmName:  01:00 02:00 ")
        self.assertEqual(d, "FilmName,a, 01:00, 02:00, ")

        #no times
        e = utils.convertToSaveForm("Screen 1 -  FilmName:  ")
        self.assertEqual(e, "FilmName,1, ")

        #no filename or times
        e = utils.convertToSaveForm("Screen 1 -  ")
        self.assertEqual(e, ",1")
