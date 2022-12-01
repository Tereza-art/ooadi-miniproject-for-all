from classes.Calendar import new_calendar
class Event:
    def __init__(self, event_id, event_time, artist, concert_hall, price, description):
        self.event_id = event_id
        self.event_time = event_time
        self.artist = artist
        self.concert_hall = concert_hall
        self.description = description
        self.price=price
        new_calendar.events.append(self)
    def __repr__(self):
        return "Id: {}, Artist: {}, Time: {}".format(
        self.event_id,    
        self.artist,
        self.event_time)  
    def __str__(self):
        return "Artist: {} \n Time: {} \n Place: {} \n Price: {} dkk \n Description: {} \n".format(
        self.artist,
        self.event_time,
        self.concert_hall,
        self.price,
        self.description)  