from sector import Sector
from sidedef import Sidedef
from enum import IntEnum

default_wall_texture = 'CEMENT1'
default_flat_texture = 'FLOOR0_1'
default_floor_height = 0
default_ceiling_height = 196


class ASC(IntEnum): # maybe these should have their own enums...
    # Linedef flags:
    IMPASSIBLE =     0x1
    BLOCK_MONSTERS = 0x2
    TWO_SIDED =      0x4  # This is done automatically
    UPPER_UNPEGGED = 0x8
    LOWER_UNPEGGED = 0x10
    SECRET_WALL =    0x20
    BLOCK_SOUND =    0x40
    NOT_ON_MAP =     0x80
    ALREADY_ON_MAP = 0x100

    # Directions:
    EAST = 0
    NORTHEAST = 45
    NORTH = 90
    NORTHWEST = 135
    WEST = 180
    SOUTHWEST = 225
    SOUTH = 270
    SOUTHEAST = 315

    # Specials:
    NONE = 0
    RANDOM_OFF = 1
    HALFSEC_BLINK = 2
    FULLSEC_BLINK = 3
    DAMAGE_BLINK = 4
    FIVETEN_DAMAGE = 5
    TWOFIVE_DAMAGE = 7
    OSCILLATE = 8
    SECRET = 9
    THIRTY_CLOSE = 10
    DEATH_END = 11
    SYNC_HALFSEC_BLINK = 12
    SYNC_FULLSEC_BLINK = 13
    THREEHUNDRED_OPEN = 14
    TENTWENTY_DAMAGE = 16
    RANDOM_FLICKER = 17  # won't work before doom v1.666


class Abstract_sector:
    def __init__(self, v0, v1, v2):
        
        # Initially only hold minimum amount to form CLOSED triangle
        self.vertices = [v0, v1, v2]
        self.sidefs = [Sidedef(0, 0,  # xy offsets
                               default_wall_texture,  # up
                               default_wall_texture,  # low
                               default_wall_texture,  # mid
                               0),  # facing sec must be updated during intermediate forming
                       Sidedef(0, 0,
                               default_wall_texture,
                               default_wall_texture,
                               default_wall_texture,
                               0),
                       Sidedef(0, 0,
                               default_wall_texture,
                               default_wall_texture,
                               default_wall_texture,
                               0)]

        self.linedef_flags = [0,0,0]

        self.floor_flat = default_flat_texture
        self.ceiling_flat = default_flat_texture

        self.floor_height = default_floor_height
        self.ceiling_height = default_ceiling_height

        self.light = 150
        self.special = 0
        self.tag_trigger = 0

        self.things = []  # Not sure whether or not this should be stored here

        self.__ffs__inverted_sector = False  # If set to true with invert(), asector is inverted

        side_num = (v1.x - v0.x)*(v2.y - v0.y) - (v2.x - v0.x)*(v1.y - v0.y)
        if side_num > 0:  # v2 on left of line0/1
            self.vertices.reverse()
        elif side_num == 0:  # v2 in line with line0/1
            print("WARNING : Formed line instead of triangle.")

    def set_floor_height(self, height):
        if height < self.ceiling_height:
            self.floor_height = height
        else:
            print("Floor higher than ceiling -> Aborted")

    def set_ceiling_height(self, height):
        if height > self.floor_height:
            self.ceiling_height = height
        else:
            print("Ceiling lower than floor -> Aborted")

    def add_thing(self, new_thing):
        self.things.append(new_thing)

    def set_upper_tex(self, sidedef_index, texture):
        self.sidefs[sidedef_index].upper_tex = texture

    def set_lower_tex(self, sidedef_index, texture):
        self.sidefs[sidedef_index].lower_tex = texture

    def set_middle_tex(self, sidedef_index, texture):
        self.sidefs[sidedef_index].middle_tex = texture

    def set_special(self, special):
    # A sector can only have one special feature
        self.special = special
        

    def add_vertex(self, vertexn, between1, between2):
        # Add a new vertex between vertices between1 & between2
        # Return True if success
        if vertexn == between1 or vertexn == between2 or between1 == between2:
            print("ERROR : goofy arguments for add_vertex.")
            return False  # throwing exceptions is for scrubs

        b1_index = -1
        b2_index = -1

        for i in range(len(self.vertices)):
            if vertexn == self.vertices[i]:  # vertex == has been overloaded
                print("WARNING : add_vertex: vertex already in abstract sector.")
                return False
            elif between1 == self.vertices[i]:
                if b1_index >= 0:
                    print("ERROR : duplicate vertices in abstract sector.")
                    return False
                b1_index = i
            elif between2 == self.vertices[i]:
                if b2_index >= 0:
                    print("ERROR : duplicate vertices in abstract sector.")
                    return False
                b2_index = i

        if b1_index >= 0 and b2_index >= 0:
            sidefn = Sidedef(0, 0,
                             default_wall_texture,
                             default_wall_texture,
                             default_wall_texture,
                             0)
            if b1_index+1 == b2_index:  # If trying to place new vert in middle
                self.vertices.insert(b2_index, vertexn)
                self.sidefs.insert(b2_index, sidefn)
                self.linedef_flags.insert(b2_index, 0)  # No flags
            elif b1_index == len(self.vertices)-1 and b2_index == 0:
                self.vertices.append(vertexn)
                self.sidefs.append(sidefn)
                self.linedef_flags.append(0)  # No flags
            else:
                print("ERROR : There is no such line in abstract sector.")
                return False

        return True

    def set_linedef_flag(self, index, flags):
        self.linedef_flags[index] = flags  # User will need to bitor old flags as required

    def invert(self):
        if not self.__ffs__inverted_sector:
            self.__ffs__inverted_sector = True
        else:
            self.__ffs__inverted_sector = False
        self.vertices.reverse()  # This happens in place
        self.sidefs.reverse()
        self.linedef_flags.reverse()

    # Called from Level.gather_data():
    def form_intermediate_representation(self):

        absec_as_sec = Sector(self.floor_height, self.ceiling_height,
                              self.floor_flat, self.ceiling_flat,
                              self.light, self.special, self.tag_trigger)

        return [self.vertices,       # 0
                absec_as_sec,        # 1
                self.sidefs,         # 2
                self.things,         # 3
                self.linedef_flags]  # 4
