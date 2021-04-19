import unittest
from utils import utils

class test_title_times_split(unittest.TestCase):

    #test the title_times_split() method 
    def test_title_times_split(self):
        #split correct ui format for ui
        aa, ab = utils.title_times_split("Screen 0 - TEST : Subtitled - 3D - Show Times -   9:00  10:00  11:00  12:00 ", True)
        self.assertEqual(aa, "Screen 0 - TEST ")
        self.assertEqual(ab, ["Screen 0 - TEST :  9:00", "Screen 0 - TEST : 10:00", "Screen 0 - TEST : 11:00", "Screen 0 - TEST : 12:00"])

        #split correct database format for database
        ba, bb = utils.title_times_split("Screen 0 - TEST :  9:00", False)
        self.assertEqual(ba, "Screen 0 - TEST ")
        self.assertEqual(bb, [" 9:00"])

        #split correct ui format for database
        ca, cb = utils.title_times_split("Screen 0 - TEST : Subtitled - 3D - Show Times -   9:00  10:00  11:00  12:00 ", False)
        self.assertEqual(ca, "Screen 0 - TEST ")
        self.assertEqual(cb, [" 9:00", "10:00", "11:00", "12:00"])

        #split correct database format for ui
        da, db = utils.title_times_split("Screen 0 - TEST :  9:00", True)
        self.assertEqual(da, "Screen 0 - TEST ")
        self.assertEqual(db, ["Screen 0 - TEST :  9:00"])

         #split ui format without times for ui
        ea, eb = utils.title_times_split("Screen 0 - TEST : Subtitled - 3D - Show Times -  ", True)
        self.assertEqual(ea, "Screen 0 - TEST ")
        self.assertEqual(eb, [])

        #split database format without times for database
        fa, fb = utils.title_times_split("Screen 0 - TEST : ", False)
        self.assertEqual(fa, "Screen 0 - TEST ")
        self.assertEqual(fb, [])

        #split ui format without screen for ui
        ga, gb = utils.title_times_split(" - TEST : Subtitled - 3D - Show Times -   9:00  10:00  11:00  12:00 ", True)
        self.assertEqual(ga, " - TEST ")
        self.assertEqual(gb, [" - TEST :  9:00", " - TEST : 10:00", " - TEST : 11:00", " - TEST : 12:00"])

        #split ui format without screen or name for ui
        ha, hb = utils.title_times_split(": Subtitled - 3D - Show Times -   9:00  10:00  11:00  12:00 ", True)
        self.assertEqual(ha, "")
        self.assertEqual(hb, [":  9:00", ": 10:00", ": 11:00", ": 12:00"])

        #split database format without screen or name for database
        ia, ib = utils.title_times_split(":  9:00", False)
        self.assertEqual(ia, "")
        self.assertEqual(ib, [" 9:00"])

        #split ui format without screen, name or time for ui
        ja, jb = utils.title_times_split(":", True)
        self.assertEqual(ja, "")
        self.assertEqual(jb, [])

        #split database format without screen, name or time for database
        ka, kb = utils.title_times_split(":", False)
        self.assertEqual(ka, "")
        self.assertEqual(kb, [])

        #split empty string for ui
        self.assertRaises(ValueError, utils.title_times_split, "", True)

        #split empty string for database
        self.assertRaises(ValueError, utils.title_times_split, "", False)