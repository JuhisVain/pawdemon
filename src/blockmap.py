import struct


class Blockmap:
    #  Used for culling collision checks
    #  HEADER - 8 bytes, 4 * 16-bit
    #  origin at bottom left corder of bottomest leftest block
    x_grid_origin
    y_grid_origin
    col_count
    row_count

    def __init__(self, x_grid_origin, y_grid_origin, col_count, row_count):
        self.x_grid_origin = x_grid_origin
        self.y_grid_origin = y_grid_origin
        self.col_count = col_count
        self.row_count = row_count
