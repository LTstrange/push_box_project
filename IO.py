def In_field():
    print("""请输入地图：
    输入详解：图中的0代表墙壁（不可移动的物块）， 3代表玩家所在位置，2代表箱子所在位置，1代表没有东西（空位）
    请逐行输入，并在输入时，将地图转换成矩形输入，周围确保有墙壁（0）包裹。输入完毕后，键入“end”以结束输入。""")
    code = 1
    T_line = []
    while True:
        line_str = input('line%d:' % (code))
        if line_str == 'end':
            return T_line
        line = [int(x) for x in line_str]
        T_line.append(line)
        code += 1