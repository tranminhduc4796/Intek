import string
import time
start_time = time.time()
maze = ['##########################################################################',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                        #',
        '#                                                                       o#',
        '##########################################################################']

maze = ['######################',
        '#  o                 #',
        '#o    A       o      #',
        '#             !      #',
        '#         !          #',
        '#                    #',
        '######################']

def get_valid_pos(maze, pos):
        valid_pos = set()
        moves = {'RIGHT': (pos[0], pos[1] + 1),
                 'LEFT': (pos[0], pos[1] - 1),
                 'UP': (pos[0] + 1, pos[1]),
                 'DOWN': (pos[0] - 1, pos[1]),
                 }
        for direction, move in moves.items():
            if maze[move[0]][move[1]] != '#' and maze[move[0]][move[1]] not in string.ascii_uppercase:
                valid_pos.add(move)
        return valid_pos

def dfs_paths(maze, start, depth):
    stack = [(start, [start])] # [('A', ['A'])]
    while stack:
        (vertex, path) = stack.pop() # vertex = 'A', path = ['A'], stack = []
                                     # vertex = 'C', path = ['A', 'C']
        # print('===================')
        # print('vertex = ', vertex, 'path = ', path)
        next_pos = get_valid_pos(maze, vertex) - set(path)
        if not next_pos: # <= Put it here not in the for loop because next_pos is None
            yield path
        # print('next_pos = ', next_pos)
        for next in next_pos: # graph[vertex] - set(path) = ['B', 'C']
            if len(path) == depth:
                yield path + [next]
            else:
                stack.append((next, path + [next])) # stack = [('B', ['A', 'B'])], stack = [('B', ['A', 'B']), ('C', ['A', 'C'])]

# for path in dfs_paths(maze, (1,1),12):
#     print(path)
print(len(list(dfs_paths(maze, (1,1), 13))))
print("--- %s seconds ---" % (time.time() - start_time))
