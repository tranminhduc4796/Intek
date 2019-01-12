from graph import RGraph
from route import Route

def findother(lst, num):
    if num == 0:
        return lst[1]
    else:
        return lst[0]

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if (start not in graph):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if (start not in graph):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

class Algo(RGraph):
    'Using A*'
    def alogorithm(self):
        object = self.trains[0]
        test = dict()
        for i in self.edges:
            for num in range(2):
                if i[num] not in test:
                    test[i[num]] = list()
                test[i[num]].append(findother(i, num))
        result = find_all_paths(test, self.routes['Pink'], self.routes['Pink'])
        # result = find_shortest_path(test, self.routes['Red'], self.routes['Blue'])
        print(result)


if __name__ == "__main__":
    graph = Algo()
    graph.build('delhi-metro-stations')
    graph.alogorithm()
