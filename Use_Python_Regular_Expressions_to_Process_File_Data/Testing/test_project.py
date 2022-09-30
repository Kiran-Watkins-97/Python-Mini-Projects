import unittest
import regex as re


class ProjectTest(unittest.TestCase):

    def test_regex(self):
        string = 'email:dfunk@exampl.org'
        expected = 'email:dfunk@exampl.org'
        actual = re.regex_email(string)
        self.assertEqual(actual, expected)

    def test_nopfx(self):
        string = 'dfunk@exampl.org'
        expected = 'email:dfunk@exampl.org'
        actual = re.regex_email(string)
        self.assertEqual(actual, expected)
