import copy

def Find_corners(field, target):
    corners = set()
    for ind_y, y in enumerate(field[1:-1]):
        for ind_x, x in enumerate(y[1:-1]):
            if x != 0:
                if field[ind_y + 2][ind_x + 1] == 0 and field[ind_y + 1 ][ind_x + 2] == 0:
                    corners.add((ind_y + 1, ind_x + 1))
                if field[ind_y + 2][ind_x + 1] == 0 and field[ind_y +1][ind_x] == 0:
                    corners.add((ind_y + 1, ind_x + 1))
                if field[ind_y][ind_x+1] == 0 and field[ind_y+1][ind_x + 2] == 0:
                    corners.add((ind_y + 1, ind_x + 1))
                if field[ind_y][ind_x+1] == 0 and field[ind_y+1][ind_x] == 0:
                    corners.add((ind_y + 1, ind_x + 1))
    diff_s = set()
    for each in corners:
        if list(each) in target:
            diff_s.add(each)
    return corners - diff_s


def check_goal(field, target):
    for each in target:
        if field[each[0]][each[1]] == 2:
            continue
        else:
            return False
    return True


def move_step(unit, step, corners):
    """
    函数内声明：
    本函数内部使用0 1 2 3，来定义上下左右的移动方向。
    其中 0对应向上U，1对应向右R，2对应向下D，3对应向左L
    :return: 移动是否有效, 新的状态
    """
    copy_unit = copy.deepcopy(unit)
    point = copy_unit.find_point()
    if step == 0:
        if copy_unit.field[point[0] - 1][point[1]] == 1:
            copy_unit.field[point[0] - 1][point[1]] = 3
            copy_unit.field[point[0]][point[1]] = 1
            copy_unit.way.append(step)
        elif copy_unit.field[point[0] - 1][point[1]] == 2:
            if copy_unit.field[point[0] - 2][point[1]] == 1:
                copy_unit.field[point[0] - 2][point[1]] = 2
                copy_unit.field[point[0] - 1][point[1]] = 3
                copy_unit.field[point[0]][point[1]] = 1
                copy_unit.way.append(step)
            else:
                return False, 0
        else:
            return False, 0
    elif step == 1:
        if copy_unit.field[point[0]][point[1] + 1] == 1:
            copy_unit.field[point[0]][point[1] + 1] = 3
            copy_unit.field[point[0]][point[1]] = 1
            copy_unit.way.append(step)
        elif copy_unit.field[point[0]][point[1] + 1] == 2:
            if copy_unit.field[point[0]][point[1] + 2] == 1:
                copy_unit.field[point[0]][point[1] + 2] = 2
                copy_unit.field[point[0]][point[1] + 1] = 3
                copy_unit.field[point[0]][point[1]] = 1
                copy_unit.way.append(step)
            else:
                return False, 0
        else:
            return False, 0
    elif step == 2:
        if copy_unit.field[point[0] + 1][point[1]] == 1:
            copy_unit.field[point[0] + 1][point[1]] = 3
            copy_unit.field[point[0]][point[1]] = 1
            copy_unit.way.append(step)
        elif copy_unit.field[point[0] + 1][point[1]] == 2:
            if copy_unit.field[point[0] + 2][point[1]] == 1:
                copy_unit.field[point[0] + 2][point[1]] = 2
                copy_unit.field[point[0] + 1][point[1]] = 3
                copy_unit.field[point[0]][point[1]] = 1
                copy_unit.way.append(step)
            else:
                return False, 0
        else:
            return False, 0
    elif step == 3:
        if copy_unit.field[point[0]][point[1] - 1] == 1:
            copy_unit.field[point[0]][point[1] - 1] = 3
            copy_unit.field[point[0]][point[1]] = 1
            copy_unit.way.append(step)
        elif copy_unit.field[point[0]][point[1] - 1] == 2:
            if copy_unit.field[point[0]][point[1] - 2] == 1:
                copy_unit.field[point[0]][point[1] - 2] = 2
                copy_unit.field[point[0]][point[1] - 1] = 3
                copy_unit.field[point[0]][point[1]] = 1
                copy_unit.way.append(step)
            else:
                return False, 0
        else:
            return False, 0
    # cut branchs and delete fail way
    for each in corners:
        if copy_unit.field[each[0]][each[1]] == 2:
            return False, 0
    if copy_unit in copy_unit.PASS_FIELD:
        return False, 0
    return True, copy_unit


def search_step(q, v, corners, target, works):
    for each in works:
        for direct in range(4):
            result = move_step(each, direct, corners)
            if result[0]:
                if check_goal(result[1].field, target):
                    v.value = 1
                    q.put(result[1])
                else:
                    q.put(result[1])
            else:
                continue

