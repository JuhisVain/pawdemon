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

    def to_binary(self):
        n_count = self.col_count * self.row_count
        #  blocklist pointers:
        blocklist_offsets = bytearray(n_count * 2)
        #  First blocklist's offset:
        offset = 4 + n_count  # 4 for header, n_count for offsets
        insert_ushort(0, blocklist_offsets, offset)

        blocklist_array = bytearray(0)

        iter_count = 2
        for blocklist in self.blocklistlist:
            blocklist_array += value_to_ushort(0) + list_to_ushort_bytes(blocklist) + value_to_ushort(65535)
            if iter_count < (n_count * 2): #  Don't do offset after last blocklist
                offset += len(blocklist) + 2  # +2 for 0x0000 & 0xFFFF
                insert_ushort(iter_count, blocklist_offsets, offset)
                iter_count += 2

        return struct.pack('<4H', self.x_grid_origin, self.y_grid_origin,
                           self.col_count, self.row_count) + blocklist_offsets + blocklist_array


def insert_ushort(index, location, ushort):
    binary_value = value_to_ushort(ushort)
    location[index] = binary_value[0]
    location[index+1] = binary_value[1]


def list_to_ushort_bytes(i_list):
    us_list = list_to_ushort(i_list)  # A list of python-bytes
    us_list_array = bytearray(0)  # an empty array to hold appended python bytes
    for element in us_list:
        us_list_array += element
    return us_list_array


def list_to_ushort(i_list):
    ushort_list = []
    for element in i_list:
        ushort_list.append(value_to_ushort(element))
    return ushort_list


def value_to_ushort(value):
    return struct.pack('<H', value)
