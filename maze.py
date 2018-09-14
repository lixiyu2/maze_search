env_data = [[3, 2, 0, 1],
            [0, 0, 0, 0],
            [2, 2, 0, 2]]
rows = len(env_data)

# TODO 2模拟环境的列数
columns = len(env_data[0])


# 计算坐标系
def move_robot(loc, act):
    move_dict = {
        'u': (-1, 0),
        'd': (1, 0),
        'l': (0, -1),
        'r': (0, 1)
    }

    return loc[0] + move_dict[act][0], loc[1] + move_dict[act][1]


def is_move_valid(loc, act):
    x, y = loc
    if act == 'u':
        x -= 1
    elif act == 'd':
        x += 1
    elif act == 'l':
        y -= 1
    elif act == 'r':
        y += 1

    return (0 <= y <= columns - 1) and (0 <= x <= rows - 1) and (env_data[x][y] != 2)


# 计算当前位置可行走的坐标
def valid_actions(env_data, loc):
    executable_action_list = []
    if is_move_valid(loc, 'u') == True:
        executable_action_list.append('u')
    if is_move_valid(loc, 'd') == True:
        executable_action_list.append('d')
    if is_move_valid(loc, 'l') == True:
        executable_action_list.append('l')
    if is_move_valid(loc, 'r') == True:
        executable_action_list.append('r')
    return executable_action_list


init = (0, 3)
end = (0, 0)
queue = [[init]]
visited = []

while queue:
    jalur = queue.pop(0)
    state = jalur[-1]
    if state == end:
        print('success')
        print(jalur)
    elif state not in visited:
        visited.append(state)
        for v in valid_actions(env_data, state):
            loc = move_robot(state, v)
            if loc not in visited:
                jalur_baru = list(jalur)
                jalur_baru.append(loc)
                queue.append(jalur_baru)
