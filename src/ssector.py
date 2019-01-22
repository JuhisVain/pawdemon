import struct


class Ssector:
    #  4 bytes: 2 shorts
    #  seg_amount: how many segments in this ssector
    #  start_seg_index: starting seg's index
    
    def __init__(self, seg_amount, start_seg_index):
        self.seg_amount = seg_amount
        self.start_seg_index = start_seg_index

    def to_binary(self):
        return struct.pack("<hh", self.seg_amount, self.start_seg_index)
