class Order:
    def __init__(self, order_id, payment_time, username, payment_status, event_id, price):
        self.order_id = order_id
        self.payment_time = payment_time
        self.username = username
        self.payment_status = payment_status
        self.event_id = event_id
        self.price = price
    def get_orderID(self):
        return self.order_id
    def get_transac_time(self):
        return self.payment_time
    def get_transac_status(self):
        return self.payment_status
    def get_event(self):
        return self.event_id
    def get_price(self):
        return self.price