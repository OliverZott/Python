import unittest
from unittest.mock import patch

# import employee
from employee import Developer, Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\nInside 'setUpClass(cls)'")

    @classmethod
    def tearDownClass(cls):
        print("\nInside 'tearDownClass(cls)'")

    def setUp(self) -> None:
        print("\nInside 'setUp(self) ...'")
        self.emp1 = Employee('Jane', 'Doe', 100000)
        self.emp2 = Developer('John', 'Doe', 100000)

    def tearDown(self) -> None:
        print("Inside 'tearDown(self) ...'")
        pass

    def test_email(self):
        print("Inside 'test_email(self) ...'")
        self.assertEqual(self.emp1.email, 'Jane.Doe@mail.com')

        self.emp2.first = 'James'
        self.assertEqual(self.emp2.email, 'James.Doe@mail.com')

    def test_fullname(self):
        print("Inside 'test_fullname(self) ...'")
        self.assertEqual(self.emp1.fullname, 'Jane Doe')
        self.emp1.first = 'Lena'
        self.assertEqual(self.emp1.fullname, 'Lena Doe')

    def test_raise(self):
        print("Inside 'test_raise(self) ...'")
        self.emp1.apply_raise()
        self.emp2.apply_raise()
        self.assertEqual(self.emp1.pay, 120000)
        self.assertEqual(self.emp2.pay, 130000)

    def test_monthly_scheduled(self):
        # mock object where it's used (employee class)
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Doe/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Doe/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == "__main__":
    unittest.main()
