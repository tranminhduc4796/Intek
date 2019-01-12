from station import Station

class Route:

    def __init__(self, name):
        self.name = name
        self.stations = []
        self.neighbors = {}

    def __repr__(self):
        return self.name

    def _add_station(self, station):
        assert (type(station) is Station), ('%s is not a station' %station)
        self.stations.append(station)


    def _add_neighbor(self, route, transfer_stn):
        assert type(route) is Route and type(transfer_stn) is Station
        if route not in self.neighbors:
            self.neighbors[route] = [transfer_stn]
        else:
            if transfer_stn not in self.neighbors[route]:
                self.neighbors[route].append(transfer_stn)
