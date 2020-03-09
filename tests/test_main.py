from inventory import *
from inventory_errors import *
from main import *
import pytest

class TestMain():
    def create_inventory(self):
        # Mains
        self.sesame_bun = Ingredient('sesame bun', 100, 2, 4, 1)
        self.brioche_bun = Ingredient('brioche bun', 100, 2, 4, 1)
        self.muffin_bun = Ingredient('muffin bun', 100, 2, 4, 1)
        self.white_wrap = Ingredient('white wrap', 100, 1, 1, 1)
        self.multigrain_wrap = Ingredient('multigrain wrap', 100, 1, 1, 1)

        self.beef_patty = Ingredient('beef patty', 100, 1, 10, 2)
        self.chicken_patty = Ingredient('chicken patty', 100, 1, 10, 2)
        self.veggie_patty = Ingredient('veggie patty', 100, 1, 10, 2)

        # Additional ingredients
        self.tomato = Ingredient('tomato', 100, 0, 5, 1)
        self.lettuce = Ingredient('lettuce', 100, 0, 5, 1)
        self.cheese = Ingredient('cheese', 100, 0, 5, 1)
        self.onion = Ingredient('onion', 100, 0, 5, 1)
        self.egg = Ingredient('egg', 100, 0, 5, 1)
        self.pineapple = Ingredient('pineapple', 100, 0, 5, 1)
        self.beetroot = Ingredient('beetroot', 100, 0, 5, 1)
        self.tomato_sauce = Ingredient('tomato sauce', 100, 0, 1, 1)
        self.bbq_sauce = Ingredient('bbq sauce', 100, 0, 1, 1)
        self.sweet_chilli_sauce = Ingredient('sweet chilli sauce', 100, 0, 1, 1)
        self.chilli_sauce = Ingredient('chilli sauce', 100, 0, 1, 1)
        self.aoli_sauce = Ingredient('aoli sauce', 100, 0, 1, 1)
    
        # Create inventory and add ingredients into inventory
        self.inventory = Inventory()
        self.inventory.add_ingredient(self.sesame_bun)
        self.inventory.add_ingredient(self.brioche_bun)
        self.inventory.add_ingredient(self.muffin_bun)
        self.inventory.add_ingredient(self.white_wrap)
        self.inventory.add_ingredient(self.multigrain_wrap)
        self.inventory.add_ingredient(self.beef_patty)
        self.inventory.add_ingredient(self.chicken_patty)
        self.inventory.add_ingredient(self.veggie_patty)
        self.inventory.add_ingredient(self.tomato)
        self.inventory.add_ingredient(self.lettuce)
        self.inventory.add_ingredient(self.onion)
        self.inventory.add_ingredient(self.cheese)
        self.inventory.add_ingredient(self.beetroot)
        self.inventory.add_ingredient(self.pineapple)
        self.inventory.add_ingredient(self.tomato_sauce)
        self.inventory.add_ingredient(self.bbq_sauce)
        self.inventory.add_ingredient(self.sweet_chilli_sauce)
    
    def test_single1(self):
        self.create_inventory()
        self.single = {'sesame bun': 2, 'beef patty': 1, 'tomato': 3, 'cheese': 3}

        self.single_burger = Single_Burger(self.single, self.inventory)
        assert self.single_burger.item_price == 13
    

    def test_double1(self):
        self.create_inventory()
        self.double = {'brioche bun': 3, 'chicken patty': 2, 'lettuce': 3, 'pineapple': 5}
    
        self.double_burger = Double_Burger(self.double, self.inventory)
        assert self.double_burger.item_price == 19
    
    def test_triple1(self):
        self.create_inventory()
        self.triple = {'muffin bun': 4, 'veggie patty': 3, 'beetroot': 2, 'tomato sauce': 1}

        self.triple_burger = Triple_Burger(self.triple, self.inventory)
        assert self.triple_burger.item_price == 18
    
    def test_wrap1(self):
        self.create_inventory()
        self.wrap = {'white wrap': 1, 'beef patty': 3, 'cheese': 2}

        self.wrap_item = Wrap(self.wrap, self.inventory)
        assert self.wrap_item.item_price == 12
    
    def test_invalid_dictionary(self):
        self.create_inventory()
        self.invalid1 = {'beef patty': 1, 'tomato sauce': 1}

        self.invalid_single = Single_Burger(self.invalid1, self.inventory)
    
    def test_invalid_instance(self):
        self.create_inventory()
        self.invalid2 = {'sesame bun': 2, 'beef patty': 1}

        self.invalid_double = Double_Burger(self.invalid2, self.inventory)
