from side_errors import *

# side class
# quantity stores quantity of item with respect to inventory system

class Side():
    def __init__(self, name, delta_quantity, inventory):
        try:
            check_all_sides_error(name, delta_quantity, inventory)
        except SideError as err:
            print (err)
        else:
            self._delta_quantity = delta_quantity
            self._price = inventory.fetch_price(name)
            self._item_price = self._delta_quantity * self._price
        
    @property
    def item_price(self):
        return self._item_price
    
    @property
    def delta_quantity(self):
        return self._delta_quantity
    
    def __str__(self):
        return f'Item Price: {self._item_price}\n'

# quantity for nuggets as the amount of the item name specified
# inventory quantity is based on whole quantities, but the
# price stored is based on price per nugget
class Nuggets(Side):
    def __init__(self, name, quantity, inventory):
        self._delta = 0 # how many nuggets to deduct
        if name == '6 Pack Nuggets':
            self._delta = quantity * 6
        if name == '3 Pack Nuggets':
            self._delta = quantity * 3
        
        super().__init__('nuggets', self._delta, inventory)

        # name should be "6 Pack Nuggets", or "3 Pack Nuggets"
        self._name = 'nuggets'
        self._quantity = quantity

    @property
    def name(self):
        return self._name   
 
    def __str__(self):
        return f'{self._name}\nQuantity: {self._quantity}\n' + super().__str__()

# sides such as fries will be need to be stocked in weight (gms)
# - small 75g
# - med 125g
# price in inventory is price/1g
class Fries(Side):
    def __init__(self, name, quantity, inventory):
        self._delta = 0 # how many grams to deduct
        if name == 'Medium Fries':
            self._delta = quantity * 125
        if name == 'Small Fries':
            self._delta = quantity * 75
        super().__init__("fries", self._delta, inventory)

        # name should be "Small Fries", or "Large Fries"
        self._name = 'fries'
        self._quantity = quantity

    @property
    def name(self):
        return self._name   
    
    def __str__(self):
        return f'{self._name}\nQuantity: {self._quantity}\n' + super().__str__()

class Drink(Side):
    def __init__(self, name, quantity, inventory):
        # delta is the same as quantity since drinks are packaged individually
        super().__init__(name, quantity, inventory)
        self._name = name
        self._quantity = quantity
    
    @property
    def name(self):
        return self._name

    def __str__(self):
        return f'{self._name}\nQuantity: {self._quantity}\n' + super().__str__()
