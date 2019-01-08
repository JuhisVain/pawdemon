import struct


class Linedef:
    #  7 * unsigned 16-bit fields
    #  start_index  index of start vertex
    #  end_index  index of end vertex
    #  flags  some special thingies
    #  line_type  effects and scripts
    #  trigger  propagates some line type "script"
    #  r_side_index  index of sidedef on the right
    #  l_side_index  index of sidedef on left OR -1 if no left sidedef
    def __init__(self, start_index, end_index, flags, line_type,
                 tag_trigger, r_side_index, l_side_index):
        self.start_index = start_index
        self.end_index = end_index
        self.flags = flags
        self.line_type = line_type
        self.tag_trigger = tag_trigger
        self.r_side_index = r_side_index
        self.l_side_index = l_side_index

    def __eq__(self, other):
        ssi = self.start_index
        sei = self.end_index
        osi = other.start_index
        oei = other.end_index
        if ssi == osi and sei == oei:
            print("Error : Duplicate start - end linedef")
            return True  # Fix if causes problems
        if ssi == oei and sei == osi:
            return True
        return False

    def set_impassible(self, bit):  # sic
        self.set_flag(0, bit)

    def set_block_monsters(self, bit):
        self.set_flag(1, bit)

    def set_two_sided(self, bit):
        self.set_flag(2, bit)

    def set_upper_unpegged(self, bit):
        self.set_flag(3, bit)

    def set_lower_unpegged(self, bit):
        self.set_flag(4, bit)

    def set_secret(self, bit):
        self.set_flag(5, bit)

    def set_block_sound(self, bit):
        self.set_flag(6, bit)

    def set_not_on_map(self, bit):
        self.set_flag(7, bit)

    def set_already_on_map(self, bit):
        self.set_flag(8, bit)

    def set_flag(self, shift, value):
        if value != 0 and value != 1:
            print("Error : Bad bit value" + str(value) +
                  "for linedef flag " + str(shift))
            return

        XORMASK = 0xffff
        shiftmask = pow(2, shift)
        value <<= shift
        self.flags = self.flags & (XORMASK ^ shiftmask) | value

    def to_binary(self):
        return struct.pack("<7h", self.start_index, self.end_index,
                           self.flags, self.line_type, self.tag_trigger,
                           self.r_side_index, self.l_side_index)
