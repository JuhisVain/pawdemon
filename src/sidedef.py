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

    def set_facing_sector(self, facing):
        self.facing_sector = facing

    def set_upper(self, texture):
        self.upper_tex = texture

    def set_lower(self, texture):
        self.lower_tex = texture

    def set_middle(self, texture):
        self.middle_tex = texture

    def to_binary(self):
        if not isinstance(self.facing_sector, int):
            print("ERROR in sidedef to binary. Facing sector not index.")
            return 'ERROR'

        return struct.pack("<hh8s8s8sh", self.x_offset, self.y_offset,
                           bytes(self.upper_tex, 'utf-8'),
                           bytes(self.lower_tex, 'utf-8'),
                           bytes(self.middle_tex, 'utf-8'),
                           self.facing_sector)
