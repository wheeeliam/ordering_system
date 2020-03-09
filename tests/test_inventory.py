from inventory import *
from inventory_errors import *
import pytest

class TestInventory():
    # Create base ingredients for inventory
    def create_ingredients(self):
        # Mains
        self.sesame_bun = Ingredient('sesame bun', 100, 2, 4, 1)
        self.brioche_bun = Ingredient('brioche bun', 100, 2, 4, 1)
        self.muffin_bun = Ingredient('muffin bun', 100, 2, 4, 1)
        self.white_wrap = Ingredient('white wrap', 100, 1, 1, 1)
        self.multigrain_wrap = Ingredient('multigrain wrap', 100, 1, 1, 1)

        self.beef_patty = Ingredient('beef patty', 100, 1, 10, 2)
        self.chicken_patty = Ingredient('chicken patty', 100, 1, 10, 2)
        self.veggie_patty = Ingredient('veggie patty', 100, 1, 10, 2)

        # Sides
        self.fries = Ingredient('fries', 1000, 0, 125, 0.02)
        self.nuggets = Ingredient('nuggets', 100, 0, 6, 0.5)
        self.coke_can = Ingredient('Coke 375ml', 100, 0, 5, 2)
        self.coke_bottle = Ingredient('Coke 600ml', 100, 0, 5, 2)
        self.orange_juice_small = Ingredient('OJ 250ml', 100, 0, 5, 2 )
        self.orange_juice_medium = Ingredient('OJ 450ml', 100, 0, 5, 2 )

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

        print(self.sesame_bun)

    # Check that an ingredient and its properties are created
    def test_ingredient_attributes(self):
        self.create_ingredients()
        assert(self.sesame_bun)
        assert(self.sesame_bun.qty_remaining == 100)
        assert(self.sesame_bun.min_qty == 2)
        assert(self.sesame_bun.max_qty == 4)
        assert(self.sesame_bun.price == 1)
    
    # Create inventory and add ingredients into inventory
    def create_inventory(self):
        self.create_ingredients()
        self.inventory = Inventory()
        self.inventory.add_ingredient(self.sesame_bun)
        self.inventory.add_ingredient(self.brioche_bun)
        self.inventory.add_ingredient(self.white_wrap)
        self.inventory.add_ingredient(self.multigrain_wrap)
        self.inventory.add_ingredient(self.beef_patty)
        self.inventory.add_ingredient(self.veggie_patty)
        self.inventory.add_ingredient(self.tomato)
        self.inventory.add_ingredient(self.lettuce)
        self.inventory.add_ingredient(self.onion)
        self.inventory.add_ingredient(self.cheese)
        self.inventory.add_ingredient(self.beetroot)
        self.inventory.add_ingredient(self.tomato_sauce)
        self.inventory.add_ingredient(self.bbq_sauce)
        self.inventory.add_ingredient(self.sweet_chilli_sauce)

        print(self.inventory)

    def test_check_remove_add_ingredients(self):
        self.create_ingredients()
        self.create_inventory()

        # Test for removed items which were originally in inventory
        self.inventory.remove_ingredient(self.beetroot)
        self.inventory.remove_ingredient(self.multigrain_wrap)
        assert(self.inventory.get_ingredient('beetroot') == False)
        assert(self.inventory.get_ingredient('multigrain wrap') == False)
        self.inventory.add_ingredient(self.beetroot)
        self.inventory.add_ingredient(self.multigrain_wrap)
        assert(self.inventory.get_ingredient('beetroot') == True)
        assert(self.inventory.get_ingredient('multigrain wrap') == True)

        # Test for items which were not in inventory to show items were removed
        assert(self.inventory.get_ingredient('aoli sauce') == False)

    def test_fetch_qty(self):
        self.create_ingredients()
        self.create_inventory()
        # Test to get quantity for ingredient in inventory
        assert(self.inventory.fetch_qty('white wrap') == 100)

        # Test to get quantity for ingredient not in inventory
        assert(self.inventory.fetch_qty('fries') == -1)

    def test_fetch_price(self):
        self.create_ingredients()
        self.create_inventory()

        # Test to retrieve price for ingredient in inventory
        assert(self.inventory.fetch_price('beef patty') == 2)

        # Test to retrieve price for ingredient not in inventory
        assert(self.inventory.get_ingredient('chicken patty') == False)
        assert(self.inventory.fetch_price('chicken patty') == -1)

    def test_validate_quantity(self):
        self.create_ingredients()
        self.create_inventory()

        # Test for desired quantity larger than max quantity
        assert(self.inventory.validate_qty('beef patty', 12) == False)
        assert(self.inventory.validate_qty('cheese', 7) == False)

        # Test for desired quantity in between max and min quantity
        assert(self.inventory.validate_qty('beef patty', 6) == True)
        assert(self.inventory.validate_qty('beef patty', 3) == True)

        # Test for desired quantity less than than min quantity
        assert(self.inventory.validate_qty('beef patty', 0) == False)
        assert(self.inventory.validate_qty('cheese', -1) == False)

    def test_decrement_quantity(self):
        self.create_ingredients()
        self.create_inventory()

        # Test normal positive integer decrement
        assert(self.inventory.get_ingredient('onion') == True)
        assert(self.inventory.fetch_qty('onion') == 100)
        self.inventory.decrement_qty('onion', 95)
        assert(self.inventory.fetch_qty('onion') == 5)

        # Test invalid negative integer decrement
        self.inventory.decrement_qty('onion', -95)
        assert(self.inventory.fetch_qty('onion') == 5)

        # Test invalid decrement where desired quantity is more than max qty
        # and also where desired quantity is more than quantity remaining
        assert(self.onion.max_qty == 5)
        self.inventory.decrement_qty('onion', 10)
        assert(self.inventory.fetch_qty('onion') == 5)

    def test_increment_quantity(self):
        self.create_ingredients()
        self.create_inventory()

        # Test normal positive integer increment
        assert(self.inventory.get_ingredient('lettuce') == True)
        assert(self.inventory.fetch_qty('lettuce') == 100)

        # Test invalid negative integer increment
        self.inventory.increment_qty('lettuce', -95)
        assert(self.inventory.fetch_qty('lettuce') == 100)
        self.inventory.increment_qty('lettuce', 95)
        assert(self.inventory.fetch_qty('lettuce') == 195)
