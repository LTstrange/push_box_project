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

