import struct

class Vertex:
    #  2 * unsigned 16-bit integer
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def to_binary(self):
        return struct.pack("<HH", self.x, self.y)
