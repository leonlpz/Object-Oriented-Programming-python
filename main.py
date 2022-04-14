#INSTANCE LEVEL
from item import Item
from phone import Phone
from keyboard import Keyboard
# __dict__ dictionary magic attribute
#print(Item.__dict__) All the attributes for Class level
#print(item1.__dict__) # All the attributes for instance level

#item1 =Item("MyItem", 750, 6)

item1 = Phone("jscPhone", 1000, 3)

item1.send_email()

item1.apply_increment(0.2)
print(item1.price)

item2 = Keyboard("jscKeyboard", 1000, 3)
item2.apply_discount()
print(item2.price)



