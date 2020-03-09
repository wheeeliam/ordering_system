from inventory import *
from order import *
from main import *
from side import *

class IdGenerator():
    def __init__(self):
        self._id = 0

    def next(self):
        self._id += 1
        return self._id

order_generator = IdGenerator()

# system class
class System():
    def __init__(self):
        # orders will be simple queue data structure. Restaurant can only
        # complete one order at a time. No parallel fulfillment of orders
        self._orders = []
        self._inventory = Inventory()
    
    # view all orders
    @property
    def orders(self):
        return self._orders

    @property
    def inventory(self):
        return self._inventory
    
    #################################
    # Order Functions
    #################################


    # create instance of order and assign to self._orders
    # orderID generated from position in the self._orders array
    def create_order_in_orders(self):
        # self._orders.append(Order(len(self._orders)))
        # return len(self._orders)-1
        self._orders.append(Order(order_generator.next()))
        return self._orders[-1].order_id

    # delete order from the front of the queue
    def delete_order_from_orders(self):
        self._orders.remove(self._orders[0])

    # remove order based on an index found from order id
    def remove_order_by_id(self, order_index):
        self._orders.remove(self._orders[order_index])

    # add items to order in self._order array
    def add_item_to_order(self, item, order_id):
        index = self.get_index_of_order_id(order_id)
        self._orders[index].append_itemlist(item)

    # returns order status
    def get_order_status(self, order_id):
        index = self.get_index_of_order_id(order_id)
        return self._orders[index].order_status

    # update order status given order_id
    def update_order_status(self, new_status, order_id):
        index = self.get_index_of_order_id(order_id)
        self._orders[index].assign_order_status(new_status)
        if new_status == "Kitchen Received":
            self._orders[index].compute_total_price()
        if new_status == "Ready for pickup":
            pass
        
    # gets index of order in orders, from order id
    # - returns false if orderid doesn't exist
    def get_index_of_order_id(self, order_id):
        for order in self._orders:
            if order_id == str(order.order_id):
                return self._orders.index(order)
    
        return False
    
    # get order object __str__ given an order_id
    def get_order_str(self, order_id):
        index = self.get_index_of_order_id(order_id)
        return (self._orders[index])
    
    # view order given an order_id
    def view_order(self, order_id):
        index = self.get_index_of_order_id(order_id)
        print (self._orders[index])
    
    # view all orders 
    def view_all_orders(self):
        for order in self.orders:
            print(order)

    #################################
    # Inventory Functions
    #################################

    # update_inventory()
    # - takes in order_id and inventory
    def update_inventory_order(self, order_id):
        index = self.get_index_of_order_id(order_id)
        itemlist = self._orders[index].itemlist
        for item in itemlist:
            if isinstance(item, Main):
                print (item.ingredients)
                for key in item.ingredients:
                    self.inventory.decrement_qty(key, item.ingredients[key])
                
            elif isinstance(item, Side):
                print (item.name)
                print (item.delta_quantity)
                self.inventory.decrement_qty(item.name, item.delta_quantity)
        

    # ingredient is Ingredient('sesame_bun', 100, 2, 4, 1)
    # - do all the adding
    def update_inventory_admin(self, ingredient):
        self._inventory.add_ingredient(ingredient)