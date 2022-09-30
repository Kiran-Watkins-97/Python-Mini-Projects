from unittest import TestCase

import main


class Test(TestCase):
    def test_square_value_positive(self):
        input_value = 100
        expected = input_value ** 2
        actual = main.square_value(input_value)
        self.assertEqual(expected, actual)

    def test_square_value_negative(self):
        input_value = -100
        expected = input_value ** 2
        actual = main.square_value(input_value)
        self.assertEqual(expected, actual)

    def test_square_value_string(self):
        # Main code casts strings as int so that it matches the specified input format
        input_value_string = "100"
        input_value = int(input_value_string)
        expected = input_value ** 2
        actual = main.square_value(input_value)
        self.assertEqual(expected, actual)
