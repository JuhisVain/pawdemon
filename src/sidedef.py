import struct


class Sidedef:
    #  30 bytes
    #  2 * 16bits, 3 * 8byteStrings, 1 * 16bits
    #  texture offsets
    #  names of textures
    #  sector that this side faces

    def __init__(self, x_offset, y_offset, upper_tex, lower_tex, middle_tex, facing_sector):
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.upper_tex = upper_tex
        self.lower_tex = lower_tex
        self.middle_tex = middle_tex
        self.facing_sector = facing_sector

    def to_binary(self):
        return struct.pack("<HH8s8s8sH", self.x_offset, self.y_offset,
                           bytes(self.upper_tex, 'utf-8'),
                           bytes(self.lower_tex, 'utf-8'),
                           bytes(self.middle_tex, 'utf-8'),
                           self.facing_sector)
