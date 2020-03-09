from system import System
from inventory import Ingredient

def bootstrap_system():
    # initialise system
    system = System()

    # intialising inventory in system
    system.update_inventory_admin(Ingredient('sesame bun', 'main', 100, 2, 4, 1))
    system.update_inventory_admin(Ingredient('brioche bun', 'main', 100, 2, 4, 1))
    system.update_inventory_admin(Ingredient('beef patty', 'main',100, 1, 10, 2))
    system.update_inventory_admin(Ingredient('chicken patty', 'main', 100, 1, 10, 2))
    system.update_inventory_admin(Ingredient('veggie patty', 'main', 100, 1, 10, 2))
    system.update_inventory_admin(Ingredient('tomato', 'main', 100, 0, 5, 1))
    system.update_inventory_admin(Ingredient('cheese', 'main', 100, 0, 5, 1))
    system.update_inventory_admin(Ingredient('wholegrain wrap', 'main', 100, 0, 1, 1))
    system.update_inventory_admin(Ingredient('nuggets', 'side', 100, 0, 12, 0.5))
    system.update_inventory_admin(Ingredient('fries', 'side', 1000, 0, 125, 0.02))
    system.update_inventory_admin(Ingredient('Coke 375ml', 'side', 100, 0, 5, 2))
    system.update_inventory_admin(Ingredient('Coke 600ml', 'side', 100, 0, 5, 2))
    system.update_inventory_admin(Ingredient('OJ 250ml', 'side', 100, 0, 5, 2 ))
    system.update_inventory_admin(Ingredient('OJ 450ml', 'side', 100, 0, 5, 2 ))
    system.update_inventory_admin(Ingredient('lettuce', 'main', 100, 0, 5, 1))
    system.update_inventory_admin(Ingredient('pineapple', 'main', 100, 0, 5, 1))
    system.update_inventory_admin(Ingredient('beetroot', 'main', 100, 0, 5, 1))
    system.update_inventory_admin(Ingredient('tomato sauce', 'main', 100, 0, 5, 1))
    system.update_inventory_admin(Ingredient('bbq sauce', 'main', 100, 0, 5, 1))
    system.update_inventory_admin(Ingredient('onion', 'main', 100, 0, 5, 1))
    system.update_inventory_admin(Ingredient('egg', 'main', 100, 0, 5, 1))
    system.update_inventory_admin(Ingredient('Chocolate Sundae Small 150ml', 'side', 100, 0, 5, 3))
    system.update_inventory_admin(Ingredient('Chocolate Sundae Medium 250ml', 'side', 100, 0, 5, 3))
    system.update_inventory_admin(Ingredient('Chocolate Sundae Large 350ml', 'side', 100, 0, 5, 3))
    system.update_inventory_admin(Ingredient('Strawberry Sundae Small 150ml', 'side', 100, 0, 5, 3))
    system.update_inventory_admin(Ingredient('Strawberry Sundae Medium 250ml', 'side', 100, 0, 5, 3))
    system.update_inventory_admin(Ingredient('Strawberry Sundae Large 350ml', 'side', 100, 0, 5, 3))









    return system
