import random
import string


class VehicleInfo:
    brand: str
    catalogue_price: int
    electric: bool

    def __init__(self, brand: str, catalogue_price: int, electric: bool) -> None:
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.electric = electric
        self.tax = self.calc_tax()

    def calc_tax(self) -> int:
        tax_percentage = 0.05
        if self.brand == "Tesla Model 3" or self.brand == "Volkswagen ID3":
            tax_percentage = 0.02

        return tax_percentage * self.catalogue_price


class Vehicle:

    def __init__(self, id: str, license_plate: str, info: object) -> None:
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def __repr__(self):
        return super().__repr__() + f"\nVehicle:   {self.info.brand}\n"


class VehicleRegistry:
    vehicle_info = {}

    def add_vehicle_info(self, brand: str, electric: bool, catalogue_price: int) -> None:
        self.vehicle_info[brand] = VehicleInfo(
            brand=brand,
            electric=electric,
            catalogue_price=catalogue_price)

    def __init__(self) -> None:
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))} "

    # @staticmethod   not possible without instantiating, because "vehicle_info" is created on instatiation
    def create_vehicle(self, brand: str):
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        vehicle = Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])
        return vehicle


class Application:

    def register_vehicle(self, brand: string):

        vehicle_registry = VehicleRegistry()
        vehicle = vehicle_registry.create_vehicle(brand)
        print(vehicle)

        print("Registration complete: Vehicle information:")
        print(f"Brand: {brand}")
        print(f"Id: {vehicle.id}")
        # print(f"Id: {vehicle[info][vehicle_id]}")
        print(f"License plate: {vehicle.license_plate}")
        print(f"Brand: {vehicle.info.brand}")
        print(f"Taxes: {vehicle.info.tax}")


if __name__ == "__main__":
    app = Application()
    app.register_vehicle("BMW 5")
