from linedef import Linedef
from sidedef import Sidedef
from vertex import Vertex
from thing import Thing


class Level:
    def __init__(self, level_number):
        self.number = level_number
        self.abstract_sectors = []

    def add_sector(self, abstract_sector):
        self.abstract_sectors.append(abstract_sector)

    # You must
    def gather_data(self):
        # before venturing forth!
        level_vertices = []
        level_linedefs = []
        level_sectors = []
        level_sidedefs = []
        level_things = []
        for absec in self.abstract_sectors:
            air = absec.form_intermediate_representation()
            vertex_index = len(level_vertices)  # start at zero, counts verts as added
            this_sector = len(level_sectors)
            level_sectors.append(air[1])  # sector
            for i in range(len(air[0])):  # vertices, sidedefs & linedefs
                level_vertices.append(air[0][i])  # vertices

                air[2][i].set_facing_sector(this_sector)  # sidedefs
                sidedef_index = len(level_sidedefs)
                level_sidedefs.append(air[2][i])

                if (i + 1) < len(air[0]):  # normie linedefs
                    level_linedefs.append(Linedef(vertex_index+i,
                                                  vertex_index+i+1,
                                                  0, 0, 0,
                                                  sidedef_index,
                                                  -1))
                elif (i + 1) == len(air[0]):  # closing linedef
                    level_linedefs.append(Linedef(vertex_index+i,
                                                  vertex_index,
                                                  0, 0, 0,
                                                  sidedef_index,
                                                  -1))

            for thing in air[3]:  # things
                level_things.append(thing)

        return [self.number,        # 0
                level_vertices,     # 1
                level_linedefs,     # 2
                level_sectors,      # 3
                level_sidedefs,     # 4
                level_things]       # 5
