import math


class Reject:
    #  Used to cull monster detection outside player's sector
    #  ( sector_count ^ 2 ) / 8 bytes, rounded up
    #  a 2d-array of booleans
    def __init__(self, sector_count):
        #  This should initialize to zeroes, meaning no culling:
        self.array = bytearray(math.ceil(math.pow(sector_count, 2) / 8))

    def to_binary(self):
        return self.array  #  That was easy. It even looks like it works
