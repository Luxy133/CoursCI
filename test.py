# test_string_utils.py

import unittest
from main import StringUtils

class TestStringUtils(unittest.TestCase):

    def test_inverser_chaine(self):
        self.assertEqual(StringUtils.inverser_chaine("abcd"), "dcba")

    def test_est_palindrome(self):
        self.assertTrue(StringUtils.est_palindrome("radar"))
        self.assertFalse(StringUtils.est_palindrome("python"))

    def test_compter_lettres(self):
        self.assertEqual(StringUtils.compter_lettres("python"), 6)

if __name__ == "__main__":
    unittest.main()
