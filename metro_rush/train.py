from station import Station
from route import Route

class Train:
    def __repr__(self):
        return str(self.id)


    def __init__(self, id):
        self.id = id
        self.current_station = None
        self.current_route = None
        self.path = []


    def move_to_route(self, route):
        assert (type(route) is Route), 'the {} is not a line'.format(route)
        self.current_route = route
        self.path.append(route)


    def move_to_station(self, station):
        assert (type(station) is Station), 'the {} is not a station'.format(station)
        if self.current_station:
            self.current_station._switch_visit()
        station._switch_visit()
        self.current_station = station
        self.path.append(station)


    def move_to(self, nxt_pos):
        if type(nxt_pos) is Route:
            self.move_to_route(nxt_pos)
        elif type(nxt_pos) is Station:
            self.move_to_station(nxt_pos)
