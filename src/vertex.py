import struct

class Vertex:
    #  2 * unsigned 16-bit integer
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_binary(self):
        return struct.pack("<HH", self.x, self.y)
