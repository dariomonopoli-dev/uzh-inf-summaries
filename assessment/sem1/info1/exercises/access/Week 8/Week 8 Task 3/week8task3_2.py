from unittest import TestCase
from week8task3_1 import calculate_factorial

class MyTests(TestCase):
    def test_None(self):
        actual=calculate_factorial(None)
        expected=None
        self.assertEqual(actual,expected)
    def test_TypeError(self):
        actual=calculate_factorial('hahaha')
        with self.assertRaises(TypeError):
            actual
    def test_ValueError(self):
        with self.assertRaises(ValueError):
             calculate_factorial(-2)
        with self.assertRaises(ValueError):
             calculate_factorial('-2')
        with self.assertRaises(ValueError):
            calculate_factorial(11)
        with self.assertRaises(ValueError):
            calculate_factorial('11')
    def test_working(self):
        actual=calculate_factorial(2.5)
        expected=2
        self.assertEqual(actual,expected)
        actual2=calculate_factorial(5)
        expected2=120
        self.assertEqual(actual2,expected2)
        actual3=calculate_factorial(0)
        expected3=1
        self.assertEqual(actual3, expected3)
    def test_invalid_too_big(self):
        with self.assertRaises(ValueError):
            calculate_factorial(11)

    def test_invalid_too_big_str(self):
        with self.assertRaises(ValueError):
            calculate_factorial("12")
    
    def test_invalid_string(self):
        with self.assertRaises(TypeError):
            calculate_factorial("abcdefg")
    def test_none(self):
        expected = None
        actual = calculate_factorial(None)
        self.assertEqual(expected,actual)
    
    def test_five(self):
        expected = 120
        actual = calculate_factorial(5)
        self.assertEqual(expected,actual)

    def test_five_str(self):
        expected = 120
        actual = calculate_factorial("5")
        self.assertEqual(expected,actual)

    def test_ten(self):
        expected = 3628800
        actual = calculate_factorial(10)
        self.assertEqual(expected,actual)

    def test_ten_str(self):
        expected = 3628800
        actual = calculate_factorial("10")
        self.assertEqual(expected,actual)

    def _assert(self, inp, expected):
        actual = calculate_factorial(inp)
        self.assertEqual(expected, actual)

    def test_None(self):
        self.assertEqual(None, calculate_factorial(None))

    def test_negative_numbers_integer(self):
        self.assertRaises(ValueError, calculate_factorial, -1)

    def test_negative_numbers_string(self):
        self.assertRaises(ValueError, calculate_factorial, "-1")

    def test_number_too_large_integer(self):
        self.assertRaises(ValueError, calculate_factorial, 11)

    def test_number_too_large_string(self):
        self.assertRaises(ValueError, calculate_factorial, "11")

    def test_string(self):
        self.assertRaises(TypeError, calculate_factorial, "s")

    def test_case_zero_integer(self):
        self._assert(0, 1)

    def test_case_zero_string(self):
        self._assert("0", 1)

    def test_larger_than_zero_integer(self):
        self._assert(7, 5040)

    def test_larger_than_zero_string(self):
        self._assert("7", 5040)

    
