import string

class Node:
    def __init__(self, pos, maze):
        self.value = maze[pos[0]][pos[1]]
        self.visited = visited
        self.pos = pos
        self.edges = []

    def get_available_moves(self, maze):
        moves = {"RIGHT": maze[self.pos[0]][self.pos[1]+1],
                 "LEFT": maze[self.pos[0]][self.pos[1]-1],
                 "DOWN": maze[self.pos[0]+1][self.pos[1]],
                 "UP": maze[self.pos[0]-1][self.pos[1]]}
        if move['RIGHT'] not in string.ascii_uppercase and move['RIGHT'] != "#":
            self.right = Nod
        if move['LEFT'] not in string.ascii_uppercase and move['LEFT'] != "#":
            self.left = left
        if move['UP'] not in string.ascii_uppercase and move['UP'] != "#":
            self.up = up
        if move['DOWN'] not in string.ascii_uppercase and move['DOWN'] != "#":
            self.down = down

class Edge:
    def __init__(self, node_from, node_to, direction):
        self.direction = direction
        self.node_from = node_from
        self.node_to = node_to

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, maze, pos):
        self.nodes.append(Node(value = maze[pos[0]][pos[1]],
                               visited = False,
                               pos = pos)

    def add_edge(self, maze, node_from, node_to):
