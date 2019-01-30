import struct

class Vertex:
    #  2 * unsigned 16-bit integer
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def to_binary(self):
        return struct.pack("<hh", self.x, self.y)
