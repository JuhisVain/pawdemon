import struct


class Node:
    #  28 bytes: 14 16-bits
    
    #  x_line_start: partitioning line's start coords
    #  y_line_start
    #  dx: distance from line_start to line's end
    #  dy:

#  BOUNDING BOXES FOR CHILD SEGS:
    #  right_y_upper:
    #  right_y_lower:
    #  right_x_lower:
    #  right_x_upper:

    #  left_y_upper:
    #  left_y_lower:
    #  left_x_lower:
    #  left_x_upper:

    #  right_child: if bit 15 = 0 : child is recursed node. if 1 child is ssector
    #  left_child:

    def __init__(self,
                 x_line_start,
                 y_line_start,
                 dx,
                 dy,

                 right_y_upper,
                 right_y_lower,
                 right_x_lower,
                 right_x_upper,

                 left_y_upper,
                 left_y_lower,
                 left_x_lower,
                 left_x_upper,

                 right_child,
                 left_child):
        self.x_line_start = x_line_start
        self.y_line_start = y_line_start
        self.dx = dx
        self.dy = dy

        self.right_y_upper = right_y_upper
        self.right_y_lower = right_y_lower
        self.right_x_lower = right_x_lower
        self.right_x_upper = right_x_upper

        self.left_y_upper = left_y_upper
        self.left_y_lower = left_y_lower
        self.left_x_lower = left_x_lower
        self.left_x_upper = left_x_upper

        self.right_child = right_child
        self.left_child = left_child

    def to_binary(self):
        return struct.pack("<14H",
                           self.x_line_start,
                           self.y_line_start,
                           self.dx, self.dy,
                           self.right_y_upper,
                           self.right_y_lower,
                           self.right_x_lower,
                           self.right_x_upper,
                           self.left_y_upper,
                           self.left_y_lower,
                           self.left_x_lower,
                           self.left_x_upper,
                           self.right_child,
                           self.left_child)
