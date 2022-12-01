class Concerthall: #a concerthall can only hold one event
    def __init__(self, concerthall_id, location, max_capacity, vip_seats, normal_seats, event):
        self.concerthall_id = concerthall_id
        self.location = location
        self.max_capacity = max_capacity
        self.vip_seats = vip_seats
        self.normal_seats = normal_seats
        self.event = event