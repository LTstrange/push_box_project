class Iter(object):
    def __init__(self, field, way):
        self.field = field
        self.way = way

    def find_point(self):
        for ind_y, Ly in enumerate(self.field):
            if 3 in Ly:
                x = Ly.index(3)
                y = ind_y
        return [y, x]

    def __eq__(self, other):
        return self.field == other.field

    def __hash__(self):
        return hash(tuple(self.field))


