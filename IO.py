def In_field():
    print("""请输入地图：
    输入详解：图中的0代表墙壁（不可移动的物块）， 3代表玩家所在位置，2代表箱子所在位置，1代表没有东西（空位）
    请逐行输入，并在输入时，将地图转换成矩形输入，周围确保有墙壁（0）包裹。输入完毕后，键入“end”以结束输入。""")
    l_num = 1
    T_line = []
    while True:
        line_str = input('line%d:' % (l_num))
        if line_str == 'end':
            return T_line
        line = [int(x) for x in line_str]
        T_line.append(line)
        l_num += 1


def In_target():
    print("""请输入目标位置：
    输入详解：输入时，请以空格为分隔，先行后列的输入目标坐标，例如，第一行第二个的坐标为“0 1”，第一行行号为零，列号同理
    在输入时，请注意输入的目标数应与箱子数一致，否则将会重新录入。输入完毕后，请键入“end”以结束输入""")
    t_num = 1
    T_target = []
    while True:
        tar_str = input('tar%d:' % (t_num))
        if tar_str == 'end':
            return T_target
        tar = [int(i) for i in tar_str.split(' ')]
        T_target.append(tar)
        t_num += 1


def In_corners():
    print("""请辅助输入地图的角落位置：
    输入形式与目标输入的格式一致，输入完毕后，请键入“end”以结束输入""")
    c_num = 1
    T_corners = []
    while True:
        cor_str = input('cor%d:' % (c_num))
        if cor_str == 'end':
            return T_corners
        cor = [int(x) for x in cor_str.split(' ')]
        T_corners.append(cor)
        c_num += 1
