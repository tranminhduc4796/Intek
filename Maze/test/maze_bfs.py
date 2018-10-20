import string
from copy import deepcopy
import time
start_time = time.time()
maze = ['####################################################################################################',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                  #',
        '#                                                                                                 o#',
        '####################################################################################################']

maze = ['######################',
        '#   #                #',
        '#   #                #',
        '#  o#                #',
        '#####                #',
        '#                    #',
        '######################']

def get_valid_pos(maze, pos):
        valid_pos = []
        moves = {'RIGHT': (pos[0], pos[1] + 1),
                 'LEFT': (pos[0], pos[1] - 1),
                 'UP': (pos[0] + 1, pos[1]),
                 'DOWN': (pos[0] - 1, pos[1]),
                 }
        for direction, move in moves.items():
            if maze[move[0]][move[1]] != '#' and maze[move[0]][move[1]] not in string.ascii_uppercase:
                valid_pos.append(move)
        return valid_pos

def bfs(maze, start_pos):
    path = [start_pos]
    queue = [path]
    visited = {start_pos}
    while queue:
        path = queue.pop(0)
        current_pos = path[-1]
        visited.update(path)
        valid_pos = get_valid_pos(maze, current_pos)
        # if len(valid_pos) == 1 and valid_pos[0] in path:
        # print('GET: ', path)
        print('LENGTH: ', len(path))
        if maze[current_pos[0]][current_pos[1]] == 'o' or maze[current_pos[0]][current_pos[1]] == '!':
            return path
        for pos in valid_pos: # valid_pos = [(1,2),(2,1)]
            if pos not in visited:
                new_path = deepcopy(path)
                new_path.append(pos)
                queue.append(new_path)
                visited.update([pos])
print(bfs(maze, (1,1)))
# print(len(maze), len(maze[0]))
print("--- %s seconds ---" % (time.time() - start_time))
