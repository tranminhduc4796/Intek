import string
from copy import deepcopy
maze = ['####################',
        '#                  #',
        '#      oo          #',
        '#                  #',
        '#                  #',
        '#              A   #',
        '#        o         #',
        '#                  #',
        '#                  #',
        '####################']

def get_pos(maze, agent):
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if maze[row][column] == agent:
                return (row,column)
    return None

def get_valid_pos(maze, pos):
        valid_pos = set()
        moves = {'RIGHT': (pos[0], pos[1] + 1),
                 'LEFT': (pos[0], pos[1] - 1),
                 'UP': (pos[0] + 1, pos[1]),
                 'DOWN': (pos[0] - 1, pos[1]),
                 }
        for direction, move in moves.items():
            if maze[move[0]][move[1]] != '#' and\
               maze[move[0]][move[1]] not in string.ascii_uppercase:
                valid_pos.add(move)
        return valid_pos

def get_next_direction(pos_agent, next_pos):
    moves = {'RIGHT': (pos_agent[0], pos_agent[1] + 1),
             'LEFT': (pos_agent[0], pos_agent[1] - 1),
             'UP': (pos_agent[0] + 1, pos_agent[1]),
             'DOWN': (pos_agent[0] - 1, pos_agent[1]),
             }
    for direction, move in moves.items():
        if next_pos == move:
            return direction

def bfs(maze, start_pos):
    path = [start_pos]
    queue = [path]
    visited = {start_pos}
    while queue:
        path = queue.pop(0)
        current_pos = path[-1]
        visited.update(path)
        valid_pos = get_valid_pos(maze, current_pos)
        if maze[current_pos[0]][current_pos[1]] == 'o' or\
           maze[current_pos[0]][current_pos[1]] == '!':
            return path
        for pos in valid_pos:
            if pos not in visited:
                new_path = deepcopy(path)
                new_path.append(pos)
                queue.append(new_path)
                visited.update([pos])

def dfs_paths(maze, start, depth):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        next_pos = get_valid_pos(maze, vertex) - set(path)
        if not next_pos:
            yield path
        for next in next_pos:
            if len(path) == depth:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def get_path_w_value(maze, path):
    path_w_value = []
    for pos in path:
        path_w_value.append(maze[pos[0]][pos[1]])
    return path_w_value
# get_effecient_dfs_paths
def get_effecient_dfs_paths(maze, dfs_paths):
    max_score = 2  # Don't care paths with only 1 score
    effecient_dfs_paths = []
    for path in dfs_paths:  # Get the highest score paths
        path_w_value = get_path_w_value(maze, path)
        current_score = path_w_value.count('o') + 2 * path_w_value.count('!')
        if max_score < current_score:
            max_score = current_score
            effecient_dfs_paths.clear()
            effecient_dfs_paths.append(path)
        elif current_score == max_score and path not in effecient_dfs_paths:
            effecient_dfs_paths.append(path)
    min_distance = 19  # 10 steps in paths => The worst case is 19 steps
    optimize_paths = []  # Paths with min steps to get max scores.
    for path in effecient_dfs_paths:
        path_w_value = get_path_w_value(maze, path)
        score_pos = [idx for idx, v in enumerate(path_w_value) if v in 'o!']
        check_ls = [0] + score_pos  # [0] is the idx of agent pos
        total_distance = 0
        for idx in range(len(check_ls) - 1):
            total_distance += check_ls[idx + 1] - check_ls[idx]
        if min_distance > total_distance:
            min_distance = total_distance
            optimize_paths.clear()
            optimize_paths.append(path)
        elif total_distance == min_distance and path not in optimize_paths:
            optimize_paths.append(path)
    print(max_score, min_distance)
    return optimize_paths


pos_agent = get_pos(maze, 'A')
test = dfs_paths(maze, pos_agent, 10)
test2 = []
for path in test:
    test2.append(path)
valid_paths = get_effecient_dfs_paths(maze, test2)
for path in valid_paths:
    print(path)
if not valid_paths:
    print('BFS')
    valid_path = bfs(maze, pos_agent)
else:
    print('DFS')
    valid_path = valid_paths[0]
print(valid_path)
next_pos = valid_path[1]
next_dir = get_next_direction(pos_agent, next_pos)
print(next_dir)

test = dfs_paths(maze, pos_agent, 10)
test2 = []
for path in test:
    test2.append(path)
valid_paths = get_effecient_dfs_paths(maze, test2)
for path in valid_paths:
    print(path)
if not valid_paths:
    print('BFS')
    valid_path = bfs(maze, pos_agent)
else:
    print('DFS')
    valid_path = valid_paths[0]
print(valid_path)
next_pos = valid_path[1]
next_dir = get_next_direction(pos_agent, next_pos)
print(next_dir)
