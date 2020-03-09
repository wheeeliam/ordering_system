from inventory_errors import *

# inventory class

# dictionary:
#   key: ingredient
#   value: array[qty_remaining, min_qty, max_qty, price]

# decrement_qty(str, int)
# increment_qty(str, int)
# display_inventory()

# This class instantiates an ingredient which is put into Inventory
# Never changes its values directly, and is not touched otherwise
class Ingredient():

    def __init__(self, name, typ, qty_remaining, min_qty, max_qty, price):
        try: 
            check_ingredient_error(name, qty_remaining, min_qty, max_qty, price)
        except ItemError as err:
            print(err)
        else:    
            self._name = name
            self._type = typ
            self._qty_remaining = qty_remaining
            self._min_qty = min_qty
            self._max_qty = max_qty
            self._price = float(price)

    @property
    def name(self):
        return self._name

    @property
    def typ(self):
        return self._type

    @property
    def qty_remaining(self):
        return self._qty_remaining

    @qty_remaining.setter
    def qty_remaining(self, new_qty):
        self._qty_remaining = new_qty

    @property
    def min_qty(self):
        return self._min_qty
    
    @property
    def max_qty(self):
        return self._max_qty
    
    @property
    def price(self):
        return self._price
    
    
    def __str__(self):
        return f"""Ingredient: {self.name}
Quantity Remaining: {self.qty_remaining}
Minimum Quantity: {self.min_qty}
Maximum Quantity: {self.max_qty}
Price: {self.price}"""

class Inventory():

    def __init__(self):
        self._dict = {}

    # Add an ingredient to inventory
    def add_ingredient(self, i):
        self._dict[i.name] = i
        print(f'Ingredient {i.name} has now been added to inventory.')

    # Remove an ingredient from inventory
    def remove_ingredient(self, i):
        self._dict[i.name] = 0
        del self._dict[i.name]
        print(f'Ingredient {i.name} has been removed from inventory.')

    # Display all information of an ingredient
    def get_ingredient(self, i):
        if i in self._dict:
           print(f'{self._dict[i]}')
           return True
        else:
           print(f'Ingredient {i} cannot be found in inventory.')
           return False

    # Check quantity of an ingredient and make sure that it exists
    def fetch_qty(self, i):
        if i in self._dict and self._dict[i].qty_remaining > 0:
            return self._dict[i].qty_remaining
        else:
            return -1

    # Fetch price of ingredient
    def fetch_price(self, i):
        if i in self._dict:
            return self._dict[i].price
        else:
            return -1
    
    # generate a list of all ingredients containing a specified type 'main' or 'side'
    def ingr_gen(self, typ):
        l = []
        for key in self._dict:
            if typ == self._dict[key].typ:
                l.append(key)
        return l
    
    # generate a menu for base items
    def base_menu_gen(self):
        menu_list = []
        for item in ['Single burger', 'Double burger', 'Triple burger', 'Wrap']:
            if 'burger' in item:
                menu_list.append(item + ', ' + self.find_default_ingr('bun') + ', ' + self.find_default_ingr('patty'))
            else:
                menu_list.append(item + ', ' + self.find_default_ingr('wrap') + ', ' + self.find_default_ingr('patty'))

        return menu_list
    
    # finds the default ingredient 
    # find the first occurrence of <string> in the keys of the self._dict
    def find_default_ingr(self, substring):
        for key in self._dict:
            if substring in key:
                return key
        
        # returns None if no string found
        return None
                
    # Validate if quantity of ingredient chosen fits within minimum and maximum quantities
    # allowed to be bought
    def validate_qty(self, i, intended_qty):
        if (intended_qty < self._dict[i].min_qty) or (intended_qty > self._dict[i].max_qty):
            # print('Input error: invalid quantity demanded.')
            return False
        else:
            return True

    # Decrement quantity of an ingredient
    def decrement_qty(self, i, qty_change):
        try:
            check_decrement_error(self._dict[i].qty_remaining, qty_change)
        except ItemError as err:
            print(err)
        else:
            self._dict[i].qty_remaining = self._dict[i].qty_remaining - qty_change
            print(f"""Ingredient {i} successfully decremented by {qty_change}.
Ingredient {i} quantity is now {self._dict[i].qty_remaining}.\n""")   

    # Increment quantity of an ingredient
    def increment_qty(self, i, qty_change):
        try:
            check_increment_error(self._dict[i].qty_remaining, qty_change)
        except ItemError as err:
            print(err)
        else:
            self._dict[i].qty_remaining = self._dict[i].qty_remaining + qty_change
            print(f"""Ingredient {i} successfully incremented by {qty_change}.
Ingredient {i} quantity is now {self._dict[i].qty_remaining}.\n""")

    # Completely update quantity of an ingredient
    def update_item_quantity(self, i, updated_qty):
        try:
            check_update_item_quantity_error(self._dict[i].qty_remaining, updated_qty)
        except ItemError as err:
            print(err)
        else:
            self._dict[i].qty_remaining = updated_qty
            print(f"""Ingredient {i} successfully updated to {updated_qty}.\n""")  

    # Display inventory
    def __str__(self):
        invent_list = ('Inventory\n' + '------------\n')
        for i in self._dict:
            invent_list += f'Ingredient: {self._dict[i].name}\nQuantity Remaining: {self._dict[i].qty_remaining}\n'
        return invent_list