from inventory import *
from inventory_errors import *
from side import *
import pytest

class Test_Side():
    def create_inventory(self):
        # Sides
        self.fries = Ingredient('fries', 1000, 0, 125, 0.02)
        self.nuggets = Ingredient('nuggets', 100, 0, 12, 0.5)
        self.coke_can = Ingredient('Coke 375ml', 100, 0, 5, 2)
        self.coke_bottle = Ingredient('Coke 600ml', 100, 0, 5, 2)
        self.orange_juice_small = Ingredient('OJ 250ml', 100, 0, 5, 2 )
        self.orange_juice_medium = Ingredient('OJ 450ml', 100, 0, 5, 2 )
    
        # Create inventory and add ingredients into inventory
        self.inventory = Inventory()
        self.inventory.add_ingredient(self.fries)
        self.inventory.add_ingredient(self.nuggets)
        self.inventory.add_ingredient(self.coke_can)
        self.inventory.add_ingredient(self.coke_bottle)
        self.inventory.add_ingredient(self.orange_juice_small)
        self.inventory.add_ingredient(self.orange_juice_medium)

    def test_small_fries(self):
        self.create_inventory()
        self.small_fries = Fries('Small Fries', 1, self.inventory)
        assert (self.small_fries.item_price == 1.5)
    
    def test_med_fries(self):
        self.create_inventory()
        self.med_fries = Fries('Medium Fries', 1, self.inventory)
        assert (self.med_fries.item_price == 2.5)
    
    def test_sixpack_nuggets(self):
        self.create_inventory()
        self.sixpack_nugs = Nuggets('6 Pack Nuggets', 2, self.inventory)
        assert (self.sixpack_nugs.item_price == 6)
    
    def test_threepack_nuggets(self):
        self.create_inventory()
        self.threepack_nuggets = Nuggets('3 Pack Nuggets', 4, self.inventory)
        assert (self.threepack_nuggets.item_price == 6)
    
    def test_coke_can(self):
        self.create_inventory()
        self.can_coke = Drink('Coke 375ml', 2, self.inventory)
        assert (self.can_coke.item_price == 4)
    
    def test_coke_bottle(self):
        self.create_inventory()
        self.bottle_coke = Drink('Coke 600ml', 2, self.inventory)
        assert (self.bottle_coke.item_price == 4)

    def test_oj_small(self):
        self.create_inventory()
        self.oj_small = Drink('OJ 250ml', 1, self.inventory)
        assert (self.oj_small.item_price == 2)
    
    def test_oj_med(self):
        self.create_inventory()
        self.oj_med = Drink('OJ 450ml', 1, self.inventory)
        assert (self.oj_med.item_price == 2)
    
    def test_incorrect_name_fries(self):
        self.create_inventory()
        self.incorrect_name_fries = Fries('Small_Fries', 1, self.inventory)
    
    def test_incorrect_qty_fries(self):
        self.create_inventory()
        self.incorrect_qty_fries = Fries('Small Fries', 1000, self.inventory)

