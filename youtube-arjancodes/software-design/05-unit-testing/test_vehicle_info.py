import unittest
from vehicle_info import VehicleInfo


class TestVehicleInfo(unittest.TestCase):

    def setUp(self) -> None:
        self.vehicle_info1 = VehicleInfo("Bmw", False, 20000)
        self.vehicle_info2 = VehicleInfo("Audi", True, 30000)

    def test_compute_tax_notelectric(self):
        tax_vehicle1 = self.vehicle_info1.compute_tax(500)
        self.assertEqual(tax_vehicle1, (20000-500)*0.05)

    def test_compute_tax_electric(self):
        tax_vehicle2 = self.vehicle_info2.compute_tax(300)
        self.assertEqual(tax_vehicle2, (30000-300)*0.02)

    def test_compute_tax_wrong_input(self):
        v = VehicleInfo("Bwm", False, 10000)
        self.assertRaises(ValueError, v.compute_tax, -500)

    def test_compute_tax_toohigh(self):
        tax_vehicle2 = self.vehicle_info2.compute_tax(30001)
        self.assertEqual(tax_vehicle2, 30000*0.02)

    def test_can_lease_true(self):
        v = VehicleInfo("Bwm", False, 50000)
        self.assertTrue(v.can_lease(100000))

    def test_can_lease_false(self):
        v = VehicleInfo("Bwm", False, 80000)
        self.assertFalse(v.can_lease(100000))

    def test_can_lease_negative_income(self):
        v = VehicleInfo("Bwm", False, 80000)
        self.assertRaises(ValueError, v.can_lease, -10000)


if __name__ == "__main__":
    unittest.main()
