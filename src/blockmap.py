import struct
import math


class Blockmap:
    #  Used for culling collision checks
    #  HEADER - 8 bytes, 4 * 16-bit
    #  origin at bottom left corder of bottomest leftest block
    #  size of block 128 x 128
    #  x_grid_origin
    #  y_grid_origin
    #  col_count
    #  row_count

    #  n = cols * rows
    #  BLOCKLIST POINTERS:
    #  16-bit offsets
    #  0: offset in 16-bits from blockmap lump start to first blocklist
    #  ...
    #  n-1: offset in 16-bits to last blocklist

    #  BLOCKLIST:
    #      16bit: 0
    #      indexes of linedefs with any part inside block
    #      16bit: -1 or 0xFFFF
    #  repeat
    
    def __init__(self, x_grid_origin, y_grid_origin, col_count, row_count):
        self.x_grid_origin = x_grid_origin
        self.y_grid_origin = y_grid_origin
        self.col_count = col_count
        self.row_count = row_count
        self.blocklistlist = []  # Will hold (col_count * row_count) lists of linedef indexes


    def finalize_offsets(self):
        

    def to_binary(self):
        n_count = col_count * row_count
        blocklist_offsets = bytearray(n_count * 2)
        insert_ushort(0, self.blocklist_offsets, 4 + n_count)  # 4 for header

        blocklist_array = bytearray(0)
        for blocklist in blocklistlist:
            blocklist_array += value_to_ushort(0) + bytearray(blocklist) + value_to_ushort(65535)
            
        for i in range(2, n_count, 2):
            insert_ushort() #  let's do this later


def insert_ushort(index, location, ushort):
    binary_value = value_to_ushort(ushort)
    location[index] = binary_value[0]
    location[index+1] = binary_value[1]


def value_to_ushort(value):
    return struct.pack('<H', value)
