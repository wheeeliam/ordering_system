from system import *
from inventory import *
from order import *
from side import *
from main import *

import py

class _System():
    def setup(self):
        self.system = System()
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
        self.fries = Ingredient('fries', 1000, 0, 125, 0.02)
        self.nuggets = Ingredient('nuggets', 100, 0, 12, 0.5)
        self.coke_can = Ingredient('Coke 375ml', 100, 0, 5, 2)
        self.coke_bottle = Ingredient('Coke 600ml', 100, 0, 5, 2)
        self.orange_juice_small = Ingredient('OJ 250ml', 100, 0, 5, 2 )
        self.orange_juice_medium = Ingredient('OJ 450ml', 100, 0, 5, 2 )

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
        self.inventory.add_ingredient(self.fries)
        self.inventory.add_ingredient(self.nuggets)
        self.inventory.add_ingredient(self.coke_can)
        self.inventory.add_ingredient(self.coke_bottle)
        self.inventory.add_ingredient(self.orange_juice_small)
        self.inventory.add_ingredient(self.orange_juice_medium)

    # need asserts in tests
        # assert length of system.orders after adding new orders
        # assert length of system.orders[x] after adding items to orders[x]

    def _add_simple_order1(self):
        self.setup()
        order_id = self.system.create_order_in_orders()
        self.single = {'sesame bun': 2, 'beef patty': 1, 'tomato': 3, 'cheese': 3} 
        self.system.add_item_to_order(Single_Burger(self.single, self.inventory), order_id)
    
    def _add_simple_order2(self):
        self.setup()
        order_id = self.system.create_order_in_orders()
        self.double = {'brioche bun': 3, 'chicken patty': 2, 'lettuce': 3, 'pineapple': 5}
        self.system.add_item_to_order(Double_Burger(self.double, self.inventory), order_id)

    def _add_remove_simple_order(self):
        self.setup()
        order_id = self.system.create_order_in_orders()
        self.single = {'sesame bun': 2, 'beef patty': 1, 'tomato': 3, 'cheese': 3} 
        self.system.add_item_to_order(Single_Burger(self.single, self.inventory), order_id)

        order_id = self.system.create_order_in_orders()
        self.double = {'brioche bun': 3, 'chicken patty': 2, 'lettuce': 3, 'pineapple': 5}
        self.system.add_item_to_order(Double_Burger(self.double, self.inventory), order_id)

        self.system.delete_order_from_orders()

    def _add_complex_order(self):
        self.setup()
        order_id = self.system.create_order_in_orders()
        self.single = {'sesame bun': 2, 'beef patty': 1, 'tomato': 3, 'cheese': 3} 
        self.system.add_item_to_order(Single_Burger(self.single, self.inventory), order_id)
        self.system.add_item_to_order(Fries('Small Fries', 1, self.inventory), order_id)

        order_id = self.system.create_order_in_orders()
        self.double = {'brioche bun': 3, 'chicken patty': 2, 'lettuce': 3, 'pineapple': 5}
        self.system.add_item_to_order(Double_Burger(self.double, self.inventory), order_id)        
        self.system.add_item_to_order(Drink('Coke 600ml', 1, self.inventory), order_id)
 
    def _progress_update(self):
        self.setup()
        order_id = self.system.create_order_in_orders()
        self.single = {'sesame bun': 2, 'beef patty': 1, 'tomato': 3, 'cheese': 3} 
        self.system.add_item_to_order(Single_Burger(self.single, self.inventory), order_id)

        self.system.update_order_status('In Progress', order_id)
        self.system.update_order_status('Ready for pickup', order_id)
        self.system.delete_order_from_orders()

        order_id = self.system.create_order_in_orders()
        self.double = {'brioche bun': 3, 'chicken patty': 2, 'lettuce': 3, 'pineapple': 5}
        self.system.add_item_to_order(Double_Burger(self.double, self.inventory), order_id)

        self.system.update_order_status('In Progress', order_id)
        self.system.update_order_status('Ready for pickup', order_id)
        self.system.delete_order_from_orders()

    def _view_order(self):
        self.setup()
        order_id = self.system.create_order_in_orders()
        self.single = {'sesame bun': 2, 'beef patty': 1, 'tomato': 3, 'cheese': 3} 
        self.system.add_item_to_order(Single_Burger(self.single, self.inventory), order_id)

        self.system.update_order_status('In Progress', order_id)
        self.system.update_order_status('Ready for pickup', order_id)
        self.system.delete_order_from_orders()

        order_id = self.system.create_order_in_orders()
        self.double = {'brioche bun': 3, 'chicken patty': 2, 'lettuce': 3, 'pineapple': 5}
        self.system.add_item_to_order(Double_Burger(self.double, self.inventory), order_id)
        
        self.system.view_order(order_id)

