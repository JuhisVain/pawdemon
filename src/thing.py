import struct


class Thing:
    #  5 unsigned 16-bit integers:
    #  x & y are position
    #  angle : What direction thing faces in degrees. 0 is east. Rounded to closest 45 by Doom.
    #                                                90 is north
    #  thing_type : Specifies what this is
    #  options : Bits 0 to 2 : what difficulties will thing spawn in. 3: deaf. 4: multiplayer
    def __init__(self, x, y, angle, thing_type, options):
        self.x = x
        self.y = y
        self.angle = angle
        self.thing_type = thing_type
        self.options = options
        
    def to_binary(self):
        return struct.pack("<5h", self.x, self.y, self.angle, self.thing_type, self.options)
        
