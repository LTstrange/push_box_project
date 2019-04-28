import multiprocessing
from Iter import Iter
from IO import In_field, In_target, In_corners
from functions import Find_corners, check_goal


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

TARGET = [[4, 3], [5, 1], [6, 5]]

# corners = 1,2 1,3 2,2 2,5 4,1 4,5 4,6 5,4 6,1 6,6

CORNER = Find_corners(field, TARGET)

iter = Iter(field, [])

print(iter.point)





