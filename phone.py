# CLASS LEVEL
from item import Item

class Phone(Item):
    pay_rate = 0.5
    def __init__(self, name: str, price: float, quantity: int, broken_phones: int = 0 ): # __init__ magic method to construct
            # Call to super funtion to have access to all attributes / methods
            super().__init__(
                name, price, quantity
            )

            # Run validations to the received arguments
            assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

            # Assaign to self object
            self.broken_phones = broken_phones