from system import System

# try not to use any other functions since the system
# is supposed to act as a level of abstraction
from inventory import Ingredient
from main import *
from side import *

# call functions from inventory

# Testing individual Ingredient class (name, qty, minqty, maxqty, price)
sesame_bun = Ingredient('sesame_bun', 'main', 100, 2, 4, 1)
beef_patty = Ingredient('beef_patty', 'main', 100, 1, 10, 2)
tomato = Ingredient('tomato', 'main', 100, 0, 5, 1)
cheese = Ingredient('cheese', 'main', 100, 0, 5, 1)
lemon = Ingredient('lemon', 'main', 100, 0, 5, 1)
wholegrain_wrap = Ingredient('wholegrain wrap', 'main', 100, 0, 1, 1)
nuggets = Ingredient('nuggets', 'side', 100, 0, 12, 0.5)
fries = Ingredient('fries', 'side', 1000, 0, 125, 0.02)
coke_can = Ingredient('Coke 375ml', 'side', 100, 0, 5, 2)
coke_bottle = Ingredient('Coke 600ml', 'side', 100, 0, 5, 2)
orange_juice_small = Ingredient('OJ 250ml', 'side', 100, 0, 5, 2 )
orange_juice_medium = Ingredient('OJ 450ml', 'side',100, 0, 5, 2 )

# initiate system
system = System()

# Adding Ingredient instances to Inventory 
print('------------------------------------------')
print('Loading ingredients into system...........')
print('------------------------------------------')
system.update_inventory_admin(sesame_bun)
system.update_inventory_admin(beef_patty)
system.update_inventory_admin(tomato)
system.update_inventory_admin(cheese)
system.update_inventory_admin(wholegrain_wrap)
system.update_inventory_admin(nuggets)
system.update_inventory_admin(fries)
system.update_inventory_admin(coke_can)
system.update_inventory_admin(coke_bottle)
system.update_inventory_admin(orange_juice_small)
system.update_inventory_admin(orange_juice_medium)

print('------------------------------------------')
print('Loading order1 into system...........')
print('------------------------------------------')

# order1 contains 
#   1 single burger with 3 tomato and 3 cheese, 
#   1 double burger with 2 tomato and 2 cheese,
#   1 wrap with 1 tomato and 1 cheese


# id is 0
order1 = system.create_order_in_orders()
assert(order1 == 1)

# ingredients declaration
single_burger1_ingredients = {'sesame_bun': 2, 'beef_patty': 1, 'tomato': 3, 'cheese': 3}
double_burger1_ingredients = {'sesame_bun': 3, 'beef_patty': 2, 'tomato': 3, 'cheese': 3}
wrap1_ingredients = {'wholegrain wrap': 1, 'tomato': 1, 'cheese': 1}

# adding to ordeR
system.add_item_to_order(Single_Burger(single_burger1_ingredients, system.inventory), order1)
system.add_item_to_order(Double_Burger(double_burger1_ingredients, system.inventory), order1)
system.add_item_to_order(Wrap(wrap1_ingredients, system.inventory), order1)
system.add_item_to_order(Fries('Small Fries', 1, system.inventory), order1)
system.add_item_to_order(Nuggets('nuggets', 6, system.inventory), order1)

# TODO
# validate quantities before confirming order, 
# do a dry run of subtraction from inventory
# if any number falls below 0, raise an error.

# view order - called through system.py
print ("UPDATING STATUS") 
system.update_order_status('Kitchen received', order1)
print ("FINISHED UPDATING STATUS")

print ('You have confirmed your order. Thank you.')

# update inventory
system.update_inventory_order(order1)

# debug
print ("before delete")
system.view_all_orders()

# ~ cooking ~

system.update_order_status('ready for pickup', order1)
print ("order status of order1")
print (system.get_order_status(order1))
system.delete_order_from_orders()

print ("after delete")
system.view_all_orders()
# theres no more orders in orderlist

# id will be 0
order2 = system.create_order_in_orders()
assert (order2 == 2)

# id will be 1
order3 = system.create_order_in_orders()
assert (order3 == 3)

# id will be 2
order4 = system.create_order_in_orders()
assert (order4 == 4)

system.delete_order_from_orders()

order5 = system.create_order_in_orders()
assert (order5 == 5)






