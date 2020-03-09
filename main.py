from main_errors import *
# main class

class Main():
    def __init__(self, ingredients, inventory, base_price):
        # assert each key in other_ingr is a an ingredient in inventory with positive qty
        # assert the value of each key is within specified range in inventory
        self._ingredients = ingredients
        self._base_price = base_price
        self._item_price = self.calc_price(inventory)
    
    @property
    def item_price(self):
        return self._item_price
    
    @property
    def ingredients(self):
        return self._ingredients
    
    # compute price of object from ingredients dict and base price
    # needs to pass in inventory because prices will be diff for different inventories
    # currently also takes into account the price of buns and patties. maybe it shouldnt
    def calc_price(self, inventory):
        total_price = self._base_price
        for key in self._ingredients:
            total_price += inventory.fetch_price(key) * self._ingredients[key]
        return total_price
    
    def __str__(self):
        return f'Ingredients: {self._ingredients}\nItem Price: {self._item_price}\n'


class Single_Burger(Main):
    def __init__(self, ingredients, inventory):
        # single burger can have 2 buns and 1 patty
        try:
            check_single_burger_error(ingredients)
            check_all_burger_error(ingredients, inventory)
        except MainError as err:
            print(err)
        else:
            super().__init__(ingredients, inventory, 3)
            self._name = "Single Burger"
        
    def __str__(self):
        return f'{self._name}\n' + super().__str__()
    
        
class Double_Burger(Main):
    def __init__(self, ingredients, inventory):
        # double burger can have 3 buns and 2 patties
        try:
            check_double_burger_error(ingredients)
            check_all_burger_error(ingredients, inventory)
        except MainError as err:
            print (err)
        else:
            super().__init__(ingredients, inventory, 4)
            self._name = "Double Burger"

    def __str__(self):
        return f'{self._name}\n' + super().__str__()
 

class Triple_Burger(Main):
    def __init__(self, ingredients, inventory):
        # triple burger can have 4 buns and 3 patties
        try:
            check_triple_burger_error(ingredients)
            check_all_burger_error(ingredients, inventory)
        except MainError as err:
            print (err)
        else:
            super().__init__(ingredients, inventory, 5)
            self._name = "Triple Burger"

    def __str__(self):
        return f'{self._name}\n' + super().__str__()

class Wrap(Main) :
    def __init__(self, ingredients, inventory):
        try:
            check_wrap_error(ingredients, inventory)
        except MainError as err:
            print (err)
        else:
            super().__init__(ingredients, inventory, 3)
            self._name = "Wrap"

    def __str__(self):
        return f'{self._name}\n' + super().__str__()