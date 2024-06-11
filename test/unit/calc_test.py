import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(7, self.calc.substract(5, -2))
        self.assertEqual(-13, self.calc.substract(-3, 10))
        self.assertEqual(6, self.calc.substract(-7, -13))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
    
    def test_power_method_returns_correct_result(self):
        self.assertEqual(25, self.calc.power(5, 2))
        self.assertEqual(1, self.calc.power(0, 0))
        self.assertEqual(0.00032, self.calc.power(5, -5))
        self.assertEqual(100000000, self.calc.power(-10, 8))
    
    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(5, self.calc.sqrt(25))
        self.assertEqual(36, self.calc.sqrt(1296))
        self.assertEqual(32, self.calc.sqrt(1024))
        self.assertEqual(9.797958971132712, self.calc.sqrt(96))
    
    def test_sqrt_method_fails_with_negative_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, -15)
        self.assertRaises(TypeError, self.calc.sqrt, -2)
        
    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, "2")
        self.assertRaises(TypeError, self.calc.sqrt, None)
    
    def test_logbase10_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.logbase10(100))
        self.assertEqual(3, self.calc.logbase10(1000))
        self.assertEqual(4, self.calc.logbase10(10000))
        self.assertEqual(2.3979400086720375, self.calc.logbase10(250))

    def test_logbase10_method_fails_with_negative_parameter(self):
        self.assertRaises(TypeError, self.calc.logbase10, -14)
        self.assertRaises(TypeError, self.calc.logbase10, 0)
        self.assertRaises(TypeError, self.calc.logbase10, -257)
        self.assertRaises(TypeError, self.calc.logbase10, -9818)

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
