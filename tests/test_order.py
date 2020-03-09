from order import Order
from order_errors import OrderError, check_assign_order_status_error

import pytest

class TestOrder():
    
    def test_order_instantiation(self):
        order_id = 1
        order = Order(order_id)
        assert order is not None
        assert order._order_id == order_id
        assert order._order_status == 'Order Received'
        assert order._total_price == 0

class TestUpdateOrderStatus():

    def test_order_update_to_received(self):
        self._test_successful_order_update('Order Received')

    def test_order_update_to_pickup(self):
        self._test_successful_order_update('Ready for Pickup')

    def test_order_update_case(self):
        self._test_successful_order_update('ORDER RECEIVED')

    def test_invalid_order_update_substring(self):
        self._test_unsuccessful_order_update('pickup')

    def test_invalid_order_status(self):
        self._test_unsuccessful_order_update('Invalid order update status')

    def test_invalid_integer_order_status(self):
        self._test_unsuccessful_order_update(12345)

    def _test_successful_order_update(self, new_status):
        order = Order(1)
        # Confirm initial order status
        assert order._order_status == 'Order Received'

        # Update order status
        order.assign_order_status(new_status)
        assert order._order_status == new_status

    def _test_unsuccessful_order_update(self, new_status):
        order = Order(1)
        # Confirm initial order status
        assert order._order_status == 'Order Received'

        # Update with incorrect order status
        try:
            order.assign_order_status(new_status)
        except OrderError as err: 
            assert(err.errors == "Specify a valid order status")

        # Order status should not have been updated    
        assert order._order_status == 'Order Received'
    