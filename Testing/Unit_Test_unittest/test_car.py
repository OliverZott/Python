"""
Unit test for car-example

- test
- debug

source: https://www.jetbrains.com/help/pycharm/testing-your-first-python-application.html


author: Oliver Zott
"""

from unittest import TestCase

from Testing import Unit_Test_unittest


class TestCar(TestCase):

    def setUp(self):
        self.car = Unit_Test_unittest.Car.Car()


class TestInit(TestCar):

    def test_initial_speed(self):
        self.assertEqual(self.car.speed, 0)

    def test_initial_odometer(self):
        self.assertEqual(self.car.odometer, 0)

    def test_initial_time(self):
        self.assertEqual(self.car.time, 0)


class TestAcceleration(TestCar):

    def test_accelerate_from_zero(self):
        self.car.accelerate()
        self.assertEqual(self.car.speed, 5)

    def test_multiple_accelerates(self):
        for _ in range(3):
            self.car.accelerate()
        self.assertEqual(self.car.speed, 15)


class TestBrake(TestCar):

    def test_brake_once(self):
        self.car.accelerate()
        self.car.brake()
        self.assertEqual(self.car.speed, 0)

    def test_brake_multiple(self):
        # first accelerate to 25
        for _ in range(5):
            self.car.accelerate()
        # break 3 times -> assume speed 10
        for _ in range(3):
            self.car.brake()
        self.assertEqual(self.car.speed, 10)

    def test_negative_speed(self):
        self.car.brake()
        self.assertEqual(self.car.speed, 0)

    def test_negative_speed_multiple_brakes(self):
        for _ in range(3):
            self.car.brake()
        self.assertEqual(self.car.speed, 0)

