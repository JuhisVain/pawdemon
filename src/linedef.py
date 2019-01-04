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

    def to_binary(self):
        return struct.pack("<7h", self.start_index, self.end_index,
                           self.flags, self.line_type, self.tag_trigger,
                           self.r_side_index, self.l_side_index)
