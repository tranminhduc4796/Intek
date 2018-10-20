maze = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', 'o', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', 'o', '#'],
        ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
        ['#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#'],
        ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', 'o', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
        ['#', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

maze = [['#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', '#', ' ', '#'],
        ['#', ' ', '#', ' ', '#', ' ', '#'],
        ['#', '#', '#', ' ', '#', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', '#', '#'],
        ['#', ' ', '#', '#', '#', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#']]
import string

def dfs(maze, start_pos, visited=[], depth=0):
    check_list = [start_pos]
    visited.append(start_pos)
    def get_valid_pos(maze, start_pos):
        row, col = start_pos
        moves = {"RIGHT": (row, col+1),
                 "LEFT": (row, col-1),
                 "DOWN": (row+1, col),
                 "UP": (row-1, col)}
        valid_pos = []
        for move in moves:
            value = maze[moves[move][0]][moves[move][1]]
            if  value != "#" and value not in string.ascii_uppercase:
                valid_pos.append(moves[move])
        return valid_pos
    valid_pos = get_valid_pos(maze, start_pos)
    # if depth
    #if depth == 11:
    print('Level', depth)
    depth += 1
    print('=====')
    # print('This is visited')
    # print(visited)
    if depth == 9 or (len(valid_pos)==1 and valid_pos[0] in visited):
        print('NOTICE:')
        print(visited)
    # print('This is valid pos')
    # print(valid_pos)
    for pos in valid_pos:
        if pos not in visited:
            if depth == 9:
                break
            check_list.extend(dfs(maze, pos, visited, depth))
    visited.pop()
    return check_list

check_list = dfs(maze, (1,1))
print('==================')
print('This is check_list')
print(check_list)
