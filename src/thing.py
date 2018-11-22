import struct


class Thing:
    #  5 unsigned 16-bit integers
    def __init__(self, x, y, angle, thing_type, options):
        self.x = x
        self.y = y
        self.angle = angle
        self.thing_type = thing_type
        self.options = options
        
    def to_binary(self):
        return struct.pack("<HHHHH", self.x, self.y, self.angle, self.thing_type, self.options)
        
