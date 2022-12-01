class Schedule: #a shedule can have many artists, an artist can only have one shedule. different artists can appear in the same event
    '''
    In the constructor of shedule, artist and event are both objects.
    '''
    def __init__(self, artist, event):
        self.artist = artist
        self.event = event