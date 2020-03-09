from inventory import *

class ItemError(Exception):

    def __init__(self, errors):
        self._errors = errors

def check_ingredient_error(name, qty_remaining, min_qty, max_qty, price):
    errors = {}

    if type(name) is not str:
        errors['invalid_name'] = "Please enter a valid string for name"

    if type(qty_remaining) is not int or qty_remaining < 0:
        errors['invalid_qty_remaining'] = "Please enter a valid int for qty_remaining"

    if type(min_qty) is not int or min_qty < 0 or min_qty > max_qty:
        errors['invalid_min_qty'] = "Please enter a valid int for min_qty"

    if type(max_qty) is not int or max_qty < 0 or max_qty < min_qty or max_qty > qty_remaining:
        errors['invalid_max_qty'] = "Please enter a valid int for max_qty"

    if price < 0:
        errors['invalid_price'] = "Please enter a valid int for price"
      
    if errors:
        raise ItemError(errors)


def check_decrement_error(qty, qty_change):
    errors = {}

    if qty < qty_change:
        errors['invalid_decrement'] = 'Quantity decremented is more than quantity remaining'

    if qty_change < 0:
        errors['invalid_qty_change'] = 'Please enter a positive quantity to decrement'

    if errors:
        raise ItemError(errors)

def check_increment_error(item, qty_change):
    errors = {}

    if qty_change < 0:
        errors['invalid_qty_change'] = 'Please enter a positive quantity to increment'

    if errors:
        raise ItemError(errors)

def check_update_item_quantity_error(item, updated_qty):
    errors = {}

    if updated_qty < 0:
        errors['invalid_qty_change'] = 'Please enter a positive quantity to update'

    if errors:
        raise ItemError(errors)
