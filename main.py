import multiprocessing
from Unit import Unit
from IO import In_field, In_target, answer
from functions import Find_corners, check_goal, move_step


# pre_field = In_field()
#
# TARGET = In_target()
#
# CORNER = In_corners()

field=[[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 1, 1, 1, 1, 0, 0],
       [0, 0, 0, 1, 0, 1, 0, 0],
       [0, 1, 0, 2, 0, 1, 3, 0],
       [0, 1, 2, 1, 1, 0, 1, 0],
       [0, 1, 1, 1, 1, 2, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0]]

TARGET = [[4, 1], [5, 1], [6, 1]]

# corners = 1,2 1,3 2,2 2,5 4,1 4,5 4,6 5,4 6,1 6,6

CORNER = Find_corners(field, TARGET)

unit1 = Unit(field, [])

unit1.PASS_FIELD.add(unit1)

unit2 = move_step(unit1, 2)[1]

print(unit2.PASS_FIELD)

unit2.PASS_FIELD.add(unit2)

print(unit1 in unit2.PASS_FIELD)

unit3 = move_step(unit2, 0)[1]

unit3.PASS_FIELD.remove(unit3)

print(unit3.PASS_FIELD)
