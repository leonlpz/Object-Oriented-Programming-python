# CLASS LEVEL
import csv

class Item:
    pay_rate = 0.8 # atribute The pay rate after 20% discount
    all = [] # atribute
    # __init__ magic method to construct
    def __init__(self, name: str, price: float, quantity: float = 0 ): 
        #print(f"An instance(object) created: {name}")
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assaign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute a list of n objects (instances)
        Item.all.append(self)
    
    @property
    def price(self):
        return self.__price

    def apply_discount(self):
       self.__price = self.__price * self.pay_rate
    
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property 
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value
        self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity 

    @classmethod # decorator useful for external data like csv, jason, ...
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod # decorator useful for variables different to the object itself
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e.: 5.0, 10.0, ...
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
             return True
        else:
            return False


    def __repr__(self): # __repr__ magic method to represent data
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f""""
        Hello Everybody.
        We have {self.name} {self.quantity} times.
        Regards, Leolpz
        """

    def __send(self): # if I use double underscore (__) it now becomes in a private method
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()

  

