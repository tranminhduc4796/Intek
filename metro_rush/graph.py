import sys
from route import Route
from station import Station
from train import Train

class RGraph:

    def __init__(self):
        self.stations  = {}
        self.routes    = {}
        self.edges     = {}
        self.trains    = []
        self.num_train = 1
        self.start_route = None
        self.start     = None
        self.end       = None


    def build(self, file):
        trans_routes = []
        try:
            with open(file, 'r') as f:
                route = None
                station = None
                line = f.readline()
                while line:
                    if line == '\n':
                        line = f.readline()
                        continue
                    line = line.rstrip()
                    if line.startswith('#'):
                        route = Route(line[1:].rstrip('Line').rstrip())
                        # self._add_route(route)
                        self.routes = route
                    elif line.startswith('START='):
                        self.__get_start_end(line, 'start')
                    elif line.startswith('END='):
                        self.__get_start_end(line, 'end')
                    elif line.startswith('TRAINS='):
                        self.num_train = int(line.split('=')[-1])
                    elif line[0].isdigit():
                        id_stn, name_stn, trans_route = self.__parse_line(line)
                        if self.__has_station(name_stn):
                            station = self.__get_station(name_stn)
                        else:
                            station = Station(name_stn)
                            # self._add_station(station)
                            self.stations = station
                        route._add_station(station)
                        if trans_route:
                            trans_routes.append([route.name,
                                                 station, trans_route])
                    line = f.readline()
            self.__get_edges(trans_routes)
            self.__update_neighbors_lines(trans_routes)
            self.__set_trains()
        except FileNotFoundError:
            print('Invalid File', file=sys.stderr)


    def summary(self):
        print('Start:', graph.start)
        print('End:', graph.end)
        print('Number of trains:', graph.num_train)
        print('='*50+'Stations'+'='*50)
        print(graph.stations)
        print('='*108)
        print('='*50+'Routes'+'='*50)
        print(graph.routes)
        print('='*108)
        print('='*50+'Edges'+'='*50)
        print(graph.edges)
        print('='*108)



    # def _add_station(self, station):
    #     assert (type(station) is Station), ('%s is not a station' %station)
    #     self.stations[station.name] = station
    #
    #
    # def _add_route(self, route):
    #     self.routes[route.name] = route


    def __setattr__(self, attribute, item):
        if attribute in self.__dict__ and attribute in ['stations', 'routes']:
            self.__dict__[attribute][item.name] = item
        else:
            self.__dict__[attribute] = item



    def __parse_line(self, line):
        transfer_route = None
        if ':Conn:' in line:
            pre_part, transfer_route = line.split(':Conn: ')
            transfer_route = transfer_route.rstrip('Line').rstrip()
            id, name = pre_part.split(':')
        else:
            id, name = line.split(':')
        return id, name, transfer_route


    def __get_edges(self, trans_routes):
        for item in trans_routes:
            src_route_name, station, dst_route_name = item
            src_route = self.routes[src_route_name]
            assert dst_route_name in self.routes, ('%s is not detected'
                                                    %(dst_route_name))
            dst_route = self.routes[dst_route_name]
            key = self._get_key_name(src_route, dst_route)
            if key not in self.edges:
                self.edges[key] = {station}
            else:
                self.edges[key].add(station)


    def __update_neighbors_lines(self, trans_routes):
        for item in trans_routes:
            src_route_name, station, dst_route_name = item
            src_route = self.routes[src_route_name]
            assert type(src_route) is Route
            assert dst_route_name in self.routes, ('%s is not detected'
                                                    %(dst_route_name))
            dst_route = self.routes[dst_route_name]
            assert type(dst_route) is Route
            src_route._add_neighbor(dst_route, station)
            dst_route._add_neighbor(src_route, station)



    def __has_station(self, name):
        return name in self.stations


    def __get_station(self, name):
        return self.stations.get(name)


    def __set_trains(self):
        for id in range(self.num_train):
            train = Train(id)
            train.move_to(self.start)
            train.move_to_route(self.start_route)
            self.trains.append(train)


    def _get_key_name(self, src, dst):
        assert type(src) is Route and type(dst) is Route
        return tuple(sorted((src, dst), key=lambda route: route.name))


    def __get_start_end(self, line, mode):
        if mode == 'start':
            line = line[len('Start='):]
            s_route, stn_id = self.__parse_start_end_line(line)
            self.start_route = self.routes[s_route]
            self.start = self.start_route.stations[stn_id-1]
        elif mode == 'end':
            line = line[len('End='):]
            s_route, stn_id = self.__parse_start_end_line(line)
            self.end = self.routes[s_route].stations[stn_id-1]


    def __parse_start_end_line(self, line):
        s_route, stn_id = line.split(':')
        s_route = s_route.rstrip('Line').rstrip()
        return s_route, int(stn_id)

if __name__ == '__main__':
    graph = RGraph()
    graph.build('delhi-metro-stations')
    graph.summary()
