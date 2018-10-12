import random

env_data = [[3, 2, 2, 2, 2, 2, 2, 2, 1],
            [0, 0, 2, 2, 2, 2, 2, 0, 0],
            [2, 0, 0, 2, 2, 2, 0, 0, 2],
            [2, 2, 0, 0, 2, 0, 0, 2, 2],
            [2, 2, 2, 0, 0, 0, 2, 2, 2]]


#TODO 1模拟环境的行数
rows = len(env_data)

#TODO 2模拟环境的列数
columns = len(env_data[0])

#TODO 3取出模拟环境第三行第六列的元素
row_3_col_6 = env_data[2][5]

print("迷宫共有", rows, "行", columns, "列，第三行第六列的元素是", row_3_col_6)


#TODO 4计算模拟环境中，第一行的的障碍物个数。
number_of_barriers_row1 = env_data[0].count(2)

#TODO 5计算模拟环境中，第三列的的障碍物个数。
# ‘*’拆分env_data的数据为集合， zip合并新的集合中的列，list转换二次统计
number_of_barriers_col3 = list(zip(*env_data))[2].count(2)

print("迷宫中，第一行共有", number_of_barriers_row1, "个障碍物，第三列共有", number_of_barriers_col3, "个障碍物。")


# 开始标记
START_VAL = 1
# 终点标记
END_VAL = 3

# 查找迷宫内所有节点找出对应value的坐标
def get_location(world, value):
    for x in range(rows):
        for y in range(columns):
            if world[x][y] == value:
                return (x, y)


loc_map = {
    'start': get_location(env_data, START_VAL),
    'destination': get_location(env_data, END_VAL)
}

robot_current_loc = loc_map['start'] #TODO 7保存机器人当前的位置


# 判断是否越界
def is_move_valid_special(loc, act):

    x, y = loc
    if act == 'u':
        x -= 1
    elif act == 'd':
        x += 1
    elif act == 'l':
        y -= 1
    elif act == 'r':
        y += 1

    # 先计算值， 再统一判断是否越界和障碍物问题
    return (0 <= y <= columns - 1) and (0 <= x <= rows - 1) and (env_data[x][y] != 2)


# 可走路线
def valid_actions(loc):
    executable_action_list = []
    if is_move_valid_special(loc, 'u') == True:
        executable_action_list.append('u')
    if is_move_valid_special(loc, 'd') == True:
        executable_action_list.append('d')
    if is_move_valid_special(loc, 'l') == True:
        executable_action_list.append('l')
    if is_move_valid_special(loc, 'r') == True:
        executable_action_list.append('r')
    return executable_action_list


##TODO 11 从头定义、实现你的函数
def move_robot(loc, act):
    # 抽象计算出上下左右的坐标
    move_dict = {
        'u': (-1, 0),
        'd': (1, 0),
        'l': (0, -1),
        'r': (0, 1)
    }

    # 直接传入的坐标进行xy的计算
    return loc[0] + move_dict[act][0], loc[1] + move_dict[act][1]


##TODO 12 从头实现你的函数
def random_choose_actions(loc):
    for i in range(30000):
        action = random.choice(valid_actions(loc))
        loc = move_robot(loc, action)
        if loc == loc_map['destination']:
            print('success')
            print(i)
            break;


# 广度优先搜索
def bfs(start_loc, end_loc):
    queue = [[start_loc]]
    visited = []
    while queue:
        jalur = queue.pop(0)
        state = jalur[-1]
        print(state)
        if state == end_loc:
            print('success')
            print(jalur)
        elif state not in visited:
            visited.append(state)
            for v in valid_actions(state):
                loc = move_robot(state, v)
                if loc not in visited:
                    jalur_baru = list(jalur)
                    jalur_baru.append(loc)
                    queue.append(jalur_baru)



if __name__ == '__main__':
    # 最优路径
    bfs(loc_map['start'], loc_map['destination'])

    # 传统走迷宫
    # random_choose_actions(robot_current_loc)