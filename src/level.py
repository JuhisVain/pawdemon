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

            if vertex_index > 0:  # ???
                vertex_index -= 1

            for i in range(len(air[0])):  # vertices, sidedefs & linedefs

                # Add vertices to SET, form linedefs:
                # Figure out starting vertex's index:
                start_vert = find_from_array(air[0][i], level_vertices)
                if start_vert == -1:
                    start_vert = vertex_index + i
                    level_vertices.append(air[0][i])  # vertices
                # else: do nothing, vertex already in array and start_vert set

                # Figure out ending vertex's index:
                if (i + 1) < len(air[0]):  # Next vert in arg array is next vert
                    
                    end_vert = find_from_array(air[0][i+1], level_vertices)
                    if end_vert == -1:
                        end_vert = vertex_index + i +1
                        level_vertices.append(air[0][i+1])  # fuck it
                elif (i + 1) == len(air[0]):  # First vert in arg array is next vert
                    end_vert = find_from_array(air[0][0], level_vertices)

                air[2][i].set_facing_sector(this_sector)  # sidedefs
                sidedef_index = len(level_sidedefs)
                level_sidedefs.append(air[2][i])

                temp_linedef = Linedef(start_vert,
                                       end_vert,
                                       0, 0, 0,
                                       sidedef_index,
                                       -1)
                temp_linedef.set_impassible(True)  # Might actually want to do this in constructor
                
                lidef_index = find_from_array(temp_linedef, level_linedefs)
                if lidef_index == -1:
                    level_linedefs.append(temp_linedef)
                else:
                    if level_linedefs[lidef_index].l_side_index != -1:
                        print("Error : Linedef already two-sided")
                        # if so, dunno how to fix
                    level_linedefs[lidef_index].l_side_index = sidedef_index
                    level_linedefs[lidef_index].set_two_sided(True)

                    
                print("linedef start: " +str(start_vert)+ ", end: " +str(end_vert)+
                      ", sidedefs R: " + str(level_linedefs[lidef_index].r_side_index)+
                      ", L: " + str(level_linedefs[lidef_index].l_side_index))

            for thing in air[3]:  # things
                level_things.append(thing)

        return [self.number,        # 0
                level_vertices,     # 1
                level_linedefs,     # 2
                level_sectors,      # 3
                level_sidedefs,     # 4
                level_things]       # 5


def find_from_array(element, array):  # from unordered array, returns index
    for i in range(len(array)):
        if element == array[i]:
            return i
    return -1
