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

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

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
        self.assertEqual(6, self.calc.multiply(3, 2))
        self.assertEqual(125, self.calc.multiply(25, 5))
    
    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())
        self.assertRaises(TypeError, self.calc.multiply, "", "")
    
    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(9, self.calc.power(3, 2))
    
    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())
        self.assertRaises(TypeError, self.calc.power, "", "")

    
    def test_raiz_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.raizCuadrada(4))
        self.assertEqual(5, self.calc.raizCuadrada(25))
    
    def test_raiz_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.raizCuadrada, "2")
        self.assertRaises(TypeError, self.calc.raizCuadrada, None)
        self.assertRaises(TypeError, self.calc.raizCuadrada, object())
        self.assertRaises(TypeError, self.calc.raizCuadrada, "")
    
    def test_logaritmo_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.logaritmo10(100))
        self.assertEqual(5, self.calc.logaritmo10(100000))

    def test_logaritmo_method_fails_with_negative_nan_parameter(self):
        #self.assertRaises(TypeError, self.calc.logaritmo10, -1)
        self.assertRaises(TypeError, self.calc.logaritmo10, "0")
        self.assertRaises(TypeError, self.calc.logaritmo10, None)
        self.assertRaises(TypeError, self.calc.logaritmo10, object())


    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
