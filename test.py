# test_string_utils.py

import unittest
from main import stringCheck

class TestStringUtils(unittest.TestCase):

    def test_inverser_chaine(self):
        self.assertEqual(stringCheck.inverser_chaine("abcd"), "dcba")

    def test_est_palindrome(self):
        self.assertTrue(stringCheck.est_palindrome("radar"))
        self.assertFalse(stringCheck.est_palindrome("python"))

    def test_compter_lettres(self):
        self.assertEqual(stringCheck.compter_lettres("python"), 6)

if __name__ == "__main__":
    unittest.main()
