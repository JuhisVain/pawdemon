

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
        level_sectors = []
        level_sidedefs = []
        level_things = []
        for absec in self.abstract_sectors:
            air = absec.form_intermediate_representation()
            for vertex in air[0]:
                level_vertices.append(vertex)
            this_sector = len(level_sectors)
            level_sectors.append(air[1])
            for sidedef in air[2]:
                sidedef.set_facing_sector(this_sector)
                level_sidedefs.append(sidedef)
            for thing in air[3]:
                level_things.append(thing)

        return [self.level_number,
                level_vertices,
                level_sectors,
                level_sidedefs,
                level_things]
