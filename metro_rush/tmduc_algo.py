from graph import RGraph
from train import Train
from route import Route
from station import Station


class BruteForce(RGraph):


    def __init__(self):
        super().__init__()
        self.solutions = []


    def _get_cross_routes(self, station):
        '''
        Get all the routes go through the station
        '''
        assert type(station) is Station
        cross_routes = set()
        for route in self.routes:
            if station in self.routes[route].stations:
                cross_routes.add(self.routes[route])
        return list(cross_routes)


    def __brute_force_routes(self, s_route, e_routes, path=[]):
        if s_route in e_routes:
            self.solutions.append(path + [s_route])
            return
        new_s_routes = [item for item in s_route.neighbors]
        for route in new_s_routes:
            path.append(s_route)
            if route not in path:
                self.__brute_force_routes(route, e_routes, path)
            path.remove(s_route)


    def __get_stn_paths(self):
        '''
        Add the transfer stations for each route in the paths
        '''
        route_ls = []
        for path in self.solutions:
            temp = []
            for idx in range(len(path) - 1):
                temp.append((path[idx+1],
                             list(self.routes[path[idx].name].neighbors[path[idx+1]])
                             ))
            route_ls.append(temp)
        return route_ls


    def __bruteforce_transf_stations(self, stn_paths):
        transf_stn_ls = []
        for route, transf_stns in stn_paths:
            if not transf_stn_ls:
                transf_stn_ls = [[(route,transf_stn)] for transf_stn in transf_stns]
            else:
                temp = []
                for sub_transf_stn in transf_stns:
                    for temp_transf_stn in transf_stn_ls:
                        visited_transf_stns = [item[1] for item in temp_transf_stn]
                        if sub_transf_stn in visited_transf_stns:
                            continue
                        temp.append(temp_transf_stn + [(route, sub_transf_stn)])
                transf_stn_ls = temp
        return transf_stn_ls


    def __bruteforce_transf_station_paths(self):
        stn_paths = self.__get_stn_paths()
        out = []
        for stn_ls in stn_paths:
            out.extend(self.__bruteforce_transf_stations(stn_ls))
        return out


    def __fill_paths_w_stations(self, paths_w_transf_stations):
        out = []
        # Add the start to each path
        for idx, _ in enumerate(paths_w_transf_stations):
            paths_w_transf_stations[idx].insert(0, (self.start_route,
                                                    self.start))
            paths_w_transf_stations[idx].append((None, self.end))
        # Fill the paths with stations
        for path in paths_w_transf_stations:
            temp = []
            for idx, hub in enumerate(path[:-1]):
                s_route, s_station = hub
                nxt_route, nxt_station = path[idx+1]
                id_start = s_route.stations.index(s_station)
                id_end = s_route.stations.index(nxt_station)

                if temp and s_station == temp[-1]:
                    temp.append(s_route)
                elif temp and s_station == temp[-2]:
                    temp.append(s_route)
                else:
                    temp.append(s_station)
                    temp.append(s_route)
                if id_start > id_end:
                    if id_end == 0:
                        # This condition to fix missing station when end id = 0
                        id_end += 1
                    temp.extend(s_route.stations[id_start-1:id_end-1:-1])
                else:
                    temp.extend(s_route.stations[id_start+1:id_end+1])
            out.append(temp)
        out = sorted(out, key=lambda item: len(item))
        return out


    def trains_reach_dest(self):
        '''
        Check if all the trains reach the destination.
        '''
        for train in self.trains:
            current_pos_train = train.path[-1]
            if current_pos_train != self.end:
                return False
        return True


    def next_visited(self, nxt_state):
        if type(nxt_state) is Route:
            return False
        else:
            return nxt_state.visited


    def pick_next_pos_for_train(self, train, filled_paths):
        current_pos_train = train.path[-1]
        # print('+'*50)
        for path in filled_paths:
            # print(path)
            if current_pos_train in path[:-1]:
                idx_pos_in_path = path.index(current_pos_train)
                nxt_pos = path[idx_pos_in_path+1]
                if type(current_pos_train) is Route:
                    current_transf_station = train.path[-2]
                    transf_station_for_route_in_path = path[idx_pos_in_path-1]
                    if current_transf_station is transf_station_for_route_in_path:
                        if type(nxt_pos) is Route:
                            return nxt_pos
                        elif not nxt_pos.visited and nxt_pos not in train.path:
                            return nxt_pos
                else:
                    if type(nxt_pos) is Route:
                        return nxt_pos
                    elif (not nxt_pos.visited and nxt_pos not in train.path or
                         nxt_pos is self.end and nxt_pos not in train.path):
                        return nxt_pos


    def move_trains(self, filled_paths):
        turn = 1
        while not self.trains_reach_dest():
            print('='*50)
            print('Turn', turn)
            for train in self.trains:
                next_pos = self.pick_next_pos_for_train(train, filled_paths)
                print('Train', train.id)
                print(train.id, next_pos)
                train.move_to(next_pos)
                print(train.id, train.path, len(train.path))
                print()
            turn += 1
            if turn == 3:
                break


    def run_algo(self):
        e_routes = self._get_cross_routes(self.end)
        self.__brute_force_routes(self.start_route, e_routes)
        # print(self.solutions)
        paths_w_transf_stations = self.__bruteforce_transf_station_paths()
        # for item in paths_w_transf_stations:
        #     print(item, len(item))
        filled_paths = self.__fill_paths_w_stations(paths_w_transf_stations)
        # filled_paths = filled_paths[:3]
        # filled_paths.reverse()
        # print(filled_paths)
        # filled_paths = [filled_paths[1], filled_paths[2]]
        # for item in filled_paths[:6]:
        #     print(item, len(item))
        #     print()
        self.move_trains(filled_paths[:6])


if __name__ == '__main__':
    algo = BruteForce()
    algo.build('delhi-metro-stations')
    algo.run_algo()
    # print(algo.bruteforce_transf_station_paths())
