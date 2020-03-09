from abc import ABC, abstractmethod
from server import app, system

class ParseError(Exception):
    '''
    Raised when a form cannot be parsed correctly or fails validation
    '''

'''
Forms
'''
class OrderStatusForm():
    def __init__(self, order_id):
        self._order_id = order_id
        self._validators = [InputRequired('Order ID cannot be empty'), OrderIDWithinBounds('Order ID must be within bounds')]
        self._errors = []
    
        self.parse()
    
    def parse(self):
        try:
            for v in self._validators:
                v.validate(self._order_id)
            
        except ParseError as pe:
            self._errors.append(str(pe))
    
    @property
    def is_valid(self):
        '''
        returns true if order_id has no errors, false otherwise
        '''
        if len(self._errors) > 0:
            return False
        else:
            return True
    
    @property
    def order_id(self):
        return self._order_id
    
    @property
    def errors(self):
        return self._errors
    
        

    

'''
Form Validators
'''
class Validator(ABC):
    def __init__(self, error_msg=''):
        self._error_msg = error_msg

    @abstractmethod
    def validate(self, raw_data):
        pass
    

class InputRequired(Validator):

    def __init__(self, error_msg='This field cannot be empty'):
        super().__init__(error_msg)

    def validate(self, raw_data):
        if raw_data is None or raw_data == '':
            raise ParseError(self._error_msg)

class OrderIDWithinBounds(Validator):
    
    def __init__(self, error_msg='Order ID must be within bounds'):
        super().__init__(error_msg)
    
    def validate(self, order_id):
        if system.get_index_of_order_id(order_id) is False:
            raise ParseError(self._error_msg)