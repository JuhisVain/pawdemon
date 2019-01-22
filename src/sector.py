import struct


class Sector:
    #  26 bytes: 2 16-bits, 2 string8s, 3 16-bits
    
    #  floor_height:
    #  ceiling_height:
    
    #  floor_flat: name of floor texture
    #  ceiling_flat: name of ceiling texture
    
    #  light: 0 = dark. 255 = light. Divided into 32 levels
    #  special: special effects
    #  tag_trigger: linked to linedefs with same tag
    
    def __init__(self, floor_height, ceiling_height, floor_flat,
                 ceiling_flat, light, special, tag_trigger):

        self.floor_height = floor_height
        self.ceiling_height = ceiling_height
        self.floor_flat = floor_flat
        self.ceiling_flat = ceiling_flat
        self.light = light
        self.special = special
        self.tag_trigger = tag_trigger

    def to_binary(self):
        return struct.pack("<hh8s8s3h",
                           self.floor_height,
                           self.ceiling_height,
                           bytes(self.floor_flat, 'utf-8'),
                           bytes(self.ceiling_flat, 'utf-8'),
                           self.light,
                           self.special,
                           self.tag_trigger)
