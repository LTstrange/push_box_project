class Iter(object):
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        return self.data[0] == other.data[0]

    def __hash__(self):
        return hash(tuple(self.data[0]))
