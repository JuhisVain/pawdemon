import struct


class seg:
    #  12 bytes, 6 * 16bits

    #  Segment of a linedef bordering subsector
    #  Stored in order determined by ssector
    
    #  start_index: vertex
    #  end_index: vertex
    #  angle: in signed: 0=east, 16384=north, -16384=south, -32768=west
    #       - in hex:    0000    4000          8000          c000
    #  linedef: this seg's linedef
    #  direction: 0 if same direction as linedef, 1 if opposite
    #  offset: distance from linedef start or end, depending on direction
    
    def __init__(self, start_index, end_index, angle, linedef, direction, offset):
        self.start_index = start_index
        self.end_index = end_index
        self.angle = angle
        self.linedef = linedef
        self.direction = direction
        self.offset = offset

    def to_binary(self):
        return struct.pack("<HHHHHH", self.start_index,
                           self.end_index, self.angle,
                           self.linedef, self.direction,
                           self.offset)
