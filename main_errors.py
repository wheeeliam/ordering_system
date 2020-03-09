from main import *

class MainError(Exception):
    
    def __init__(self, errors):
        self._errors = errors

# only one type of bun and patty is allowed per burger
# the type of bun (key) and quantity (value) are stored in the first dict entry only
# the type of patty (key) and quantity (value) are stored in the second dict entry only

def check_all_burger_error(ingredients, inventory):
    errors = {}

    bun_key = list(ingredients.keys())[0]
    patty_key = list(ingredients.keys())[1]
    
    if 'bun' not in bun_key:
        errors['invalid_bun'] = "No Bun detected"
    if 'patty' not in patty_key:
        errors['invalid_patty'] = "No patty detected"

    # occurrence of 'bun' and 'patty' must not be greater than 1 in the list of keys
    bun_appearances = 0
    patty_appearances = 0
    key_list = list(ingredients.keys())

    for item in key_list:
        if 'bun' in item:
            bun_appearances += 1
        if 'patty' in item:
            patty_appearances += 1
        if (inventory.fetch_qty(item) == -1):
            errors['ingredient_unfetchable'] = "Ingredient does not exist or has invalid qty"
        if (inventory.validate_qty(item, ingredients[item]) == False):
            errors['ingredient_invalid'] = "Ingredient quantity falls out of max/min bounds"

    if bun_appearances > 1:
        errors['excess_bun_entries'] = "Only one entry allowed for buns"
    if patty_appearances > 1:
        errors['excess_patty_entries'] = "Only one entry allowed for patties"
    
    if (errors):
        raise MainError(errors)
    
def check_single_burger_error(ingredients):
    errors = {}

    # if amount of buns is not 2
    if ingredients[list(ingredients.keys())[0]] != 2:
        errors['invalid_bun_count'] = "Bun count for Single Burger must be 2"
    # if amount of patties is not 1
    if ingredients[list(ingredients.keys())[1]] != 1:
        errors['invalid_patty_count'] = "Patty count for Single Burger must be 1"
    
    if (errors):
        raise MainError(errors)

def check_double_burger_error(ingredients):
    errors = {}

    # if amount of buns is not 3
    if ingredients[list(ingredients.keys())[0]] != 3:
        errors['invalid_bun_count'] = "Bun count for Double Burger must be 3"
    # if amount of patties is not 1
    if ingredients[list(ingredients.keys())[1]] != 2:
        errors['invalid_patty_count'] = "Patty count for Double Burger must be 2"
    
    if (errors):
        raise MainError(errors)
 
def check_triple_burger_error(ingredients):
    errors = {}

    # if amount of buns is not 4
    if ingredients[list(ingredients.keys())[0]] != 4:
        errors['invalid_bun_count'] = "Bun count for Triple Burger must be 4"
    # if amount of patties is not 1
    if ingredients[list(ingredients.keys())[1]] != 3:
        errors['invalid_patty_count'] = "Patty count for Triple Burger must be 3"
    
    if (errors):
        raise MainError(errors)
 

def check_wrap_error(ingredients, inventory):
    errors = {}

    wrap_key = list(ingredients.keys())[0]
    if 'wrap' not in wrap_key:
        errors['invalid_wrap'] = "No Wrap detected"
    
    if ingredients[wrap_key] != 1:
        errors['invalid_wrap_count'] = "Wrap count must be 1"
    
    wrap_appearances = 0
    key_list = list(ingredients.keys())
    for item in key_list:
        if 'wrap' in item:
            wrap_appearances += 1
        if (inventory.fetch_qty(item) == -1):
            errors['ingredient_unfetchable'] = 'Ingredient does not exist or has invalid qty'
        if (inventory.validate_qty(item, ingredients[item]) == False):
            errors['ingredient_invalid'] = "Ingredient quantity falls out of max/min bounds"
    
    if wrap_appearances > 1:
        errors['excess_wrap_entries'] = "Only one entry allowed for wraps"
    
    if (errors):
        raise MainError(errors)
    

