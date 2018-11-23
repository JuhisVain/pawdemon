import math


def seg_distance(line_x, line_y, seg_x, seg_y):
    return math.sqrt(math.pow(seg_x - line_x, 2) + math.pow(seg_y - line_y, 2))


def seg_angle(line_x, line_y, seg_x, seg_y):
    return ((math.atan2(seg_y - line_y, (-(seg_x - line_x)))/(math.pi/2)) * 16384 )
