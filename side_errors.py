from side import *

class SideError(Exception):
    
    def __init__(self, errors):
        self._errors = errors


def check_all_sides_error(name, quantity, inventory):
    errors = {}
    
    if (inventory.fetch_qty(name) == -1):
        errors['ingredient_unfetchable'] = "Ingredient does not exist or has invalid qty"
    if (inventory.validate_qty(name, quantity) == False):
        errors['ingredient_invalid'] = "Ingredient quantity falls out of max/min bounds"
    
    if (errors):
        raise SideError(errors)
