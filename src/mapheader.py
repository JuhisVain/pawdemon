import struct


class Mapheader:
    def __init__(self, map_string):
        self.map_string = map_string

    def to_binary(self):
        return bytes(self.map_string, 'utf-8')
