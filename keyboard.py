# CLASS LEVEL
from item import Item

class Keyboard(Item):
    pay_rate = 0.7
    def __init__(self, name: str, price: float, quantity: int = 0 ): # __init__ magic method to construct
            # Call to super funtion to have access to all attributes / methods
            super().__init__(
                name, price, quantity
            )
