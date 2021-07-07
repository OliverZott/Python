import unittest
import calc
import sys

# print(sys.path)


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(3, 5), 8)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-2, -1), -3)

    def test_substract(self):
        self.assertEqual(calc.substract(3, 5), -2)
        self.assertEqual(calc.substract(1, -1), 2)
        self.assertEqual(calc.substract(-2, 1), -3)

    def test_multiply(self):
        self.assertEqual(calc.multiply(3, 5), 15)
        self.assertEqual(calc.multiply(2, -1), -2)
        self.assertEqual(calc.multiply(-2, -2), 4)

    def test_divide(self):
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-2, -1), 2)

        # cannot pass args in method, because exception will be thrown and tets not passed
        self.assertRaises(ValueError, calc.divide, 10, 0)

        # Better! : use context manager
        with self.assertRaises(ValueError):
            calc.divide(31, 0)


if __name__ == "__main__":
    unittest.main()
