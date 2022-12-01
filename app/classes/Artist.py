#object as attribute    
class Artist:
    def __init__(self, artist_id, name, shedule):
        self.artist_id = artist_id
        self.name = name
        self.shedule = shedule
    def get_artist(self):
        return "Name: {}, Email: {}, Phone: {}".format(
        self.artist_id,
        self.name,
        self.shedule)  
    def set_artist_name(self, new_name):
        self.name = new_name
    def reshedule_artist(self, new_shedule):
        self.shedule = new_shedule