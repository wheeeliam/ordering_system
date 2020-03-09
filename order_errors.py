class OrderError(Exception):

    def __init__(self, errors, msg=None):
        if msg is None:
            msg = "Order validation error occurred"
        super().__init__(msg)
        self.errors = errors

def check_assign_order_status_error(new_status):
    # User can't enter an int as an order status
    if isinstance(new_status, int):
        raise OrderError("Specify a valid order status")

    # Tests for correct string inputs
    status = new_status.lower()
    if status != "customer is making" and status != "kitchen received" and status != "ready for pickup":
        raise OrderError("Specify a valid order status")

