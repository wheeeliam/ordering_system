# order class

from order_errors import OrderError, check_assign_order_status_error

class Order():

    def __init__(self, order_id):
        self._order_id = order_id
        self._order_status = 'Customer is making'
        self._total_price = 0
        self._itemlist = []

    @property
    def order_id(self):
        return self._order_id

    @property
    def order_status(self):
        return self._order_status

    @property
    def total_price(self):
        return self._total_price
    
    @property
    def itemlist(self):
        return self._itemlist

    def assign_order_status(self, new_status):
        try:
             check_assign_order_status_error(new_status)
        except OrderError as err:
            print(err.errors)
            return None, err.errors

        self._order_status = new_status

    # append an object to itemlist
    def append_itemlist(self, item):
        self._itemlist.append(item)

    # computes total price from items in itemlist
    def compute_total_price(self):
        self._total_price = 0
        for item in self._itemlist:
            self._total_price += item.item_price
     

    # display order function
    def __str__(self):
        ret_string = ('------------------------------------------\n' + 
            f'Order ID: {self.order_id}\n'
            f'Order Status: {self._order_status}\n')
        # add in order status and order ID
        item_no = 1
        for item in self._itemlist:
            ret_string += f'Item No: {item_no}\n{item}\n'
            item_no += 1
        
        ret_string += f'Total Price: {self._total_price}\n'
        ret_string += '------------------------------------------\n'
        return ret_string