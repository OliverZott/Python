class VehicleInfo:
    brand: str
    electric: bool
    catalogue_price: int

    def __init__(self, brand: str, electric: bool, catalogue_price: int) -> None:
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    def compute_tax(self, tax_exemption_amount: int = 0) -> float:
        if tax_exemption_amount < 0:
            raise ValueError(
                f"Tax exemption amount must be positive number. {tax_exemption_amount} was given!")
        tax_percentage = 0.05

        if self.electric:
            tax_percentage = 0.02

        return tax_percentage * (self.catalogue_price - tax_exemption_amount)

    def can_lease(self, year_income: int) -> bool:
        pass


v = VehicleInfo("Bmw", False, 20000)

print(f"BMW tax: {v.compute_tax()}")
