"""
Run in terminal: 
    change to folder and run in terminal (pytest also runs std lib unittest files)
    - $ pytest 

Run in vs code:
    open Unittesting folder directly in vs code:
    - Ctrl + Shift + P
    - select pytest
    - select tests folder
    - run in "Testing" on left hand side

"""

import unittest

from fastvector import Vector2D


class VectorTests(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector2D(0, 0)
        self.v2 = Vector2D(-1, 1)
        self.v3 = Vector2D(1.5, -2.5)

    def test_equality(self) -> None:
        self.assertNotEqual(self.v1, self.v2)
        expected_result = Vector2D(-1, 1)
        self.assertEqual(self.v2, expected_result)

    def test_add(self) -> None:
        result = self.v1 + self.v2
        expected_result = Vector2D(-1, 1)
        self.assertEqual(result, expected_result)

    def test_sub(self) -> None:
        result = self.v1 - self.v2
        expected_result = Vector2D(1, -1)
        self.assertEqual(result, expected_result)

    def test_mul(self) -> None:
        result = self.v2 * 2
        expected_result = Vector2D(-2, 2)
        self.assertEqual(result, expected_result)

    def test_scalar_mul(self) -> None:
        result = self.v2 * self.v3
        expected_result = Vector2D(-1, 2)
        self.assertEqual(result, expected_result)

    def test_div(self) -> None:
        result = self.v2 / -2
        expected_result = Vector2D(0.5, -0.5)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
