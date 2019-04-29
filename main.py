import multiprocessing as mp
import copy
from Unit import Unit
from IO import In_field, In_target, answer
from functions import Find_corners, check_goal, search_step, move_step

# corners = 1,2 1,3 2,2 2,5 4,1 4,5 4,6 5,4 6,1 6,6


if __name__ == '__main__':
    pre_field = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 3, 1, 1, 1, 1, 1, 1, 0],
                 [0, 1, 2, 2, 1, 2, 2, 1, 0],
                 [0, 2, 1, 1, 1, 1, 2, 1, 0],
                 [0, 1, 2, 2, 1, 2, 2, 1, 0],
                 [0, 1, 2, 1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # pre_field = In_field()

    TARGET = [[1, 3], [2, 4], [4, 4], [5, 3], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7]]

    # TARGET = In_target()

    CORNERS = Find_corners(pre_field, TARGET)

    unit = Unit(pre_field, [])

    works = set([unit])

    q = mp.Queue()
    v = mp.Value('i', 0)
    count_step = 1
    while not v.value:
        print("step:", count_step, "works space:", len(works))
        count_step += 1
        l_works = list(works)
        p0 = mp.Process(target=search_step, args=(q, v, CORNERS, TARGET, l_works[:len(works)//4]))
        p1 = mp.Process(target=search_step, args=(q, v, CORNERS, TARGET, l_works[len(works)//4:len(works)//4*2]))
        p2 = mp.Process(target=search_step, args=(q, v, CORNERS, TARGET, l_works[(len(works)//4)*2:(len(works)//4)*3]))
        p3 = mp.Process(target=search_step, args=(q, v, CORNERS, TARGET, l_works[(len(works)//4)*3:]))
        p0.start()
        p1.start()
        p2.start()
        p3.start()
        p3.join()
        p2.join()
        p1.join()
        p0.join()
        works.clear()
        while not q.empty():
            u = q.get()
            u.PASS_FIELD.add(u)
            works.add(u)
        for e in works:
            if check_goal(e.field, TARGET):
                answer(e.way)

    c_u = Unit(pre_field, [])
    for e in works:
        for s in e.way:
            move_step(c_u, s, CORNERS)


