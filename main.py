import multiprocessing as mp
from Unit import Unit
from IO import In_field, In_target, answer
from functions import Find_corners, check_goal, search_step, move_step

# corners = 1,2 1,3 2,2 2,5 4,1 4,5 4,6 5,4 6,1 6,6


if __name__ == '__main__':
    pre_field=[[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, 0, 0, 0, 0],
               [0, 0, 1, 1, 1, 1, 0, 0],
               [0, 0, 0, 1, 0, 1, 0, 0],
               [0, 1, 0, 2, 0, 1, 3, 0],
               [0, 1, 2, 1, 1, 0, 1, 0],
               [0, 1, 1, 1, 1, 2, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

    TARGET = [[4, 1], [5, 1], [6, 1]]

    CORNERS = Find_corners(pre_field, TARGET)

    unit = Unit(pre_field, [])

    q = mp.Queue()
    v = mp.Value('i', 0)
    p = mp.Process(target=search_step, args=(q, v, CORNERS, TARGET, [unit]))
    p.start()
    p.join()
    # search_step(q, v, CORNERS, TARGET, [unit])

    # print(unit.way)
    while not q.empty():
        u = q.get()
        u.PASS_FIELD.add(u)
    for e in unit.PASS_FIELD:
        print(e)


