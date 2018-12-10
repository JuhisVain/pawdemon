import math


class Level:
    def __init__(self, doom_version, level_number):
        self.mapheader = 'TEMPx'
        if doom_version == 1:
            self.mapheader = doom1_head(level_number)
        elif doom_version == 2:
            self.mapheader = doom2_head(level_number)

        self.abstract_sectors = []

    def add_sector(self, abstract_sector):
        self.abstract_sectors.append(abstract_sector)


def doom1_head(level_number):
    if level_number < 1 or level_number > 36:
        print('Level index error: ' + level_number)
        return 'd1hE'
    level_number -= 1
    d1head = 'E' + str((math.floor(level_number / 9)+1))
    d1head += 'M' + str((level_number % 9)+1)
    return d1head


def doom2_head(level_number):
    if level_number < 1 or level_number > 36:
        print('Level index error: ' + level_number)
        return 'd2hER'
    d2head = 'uninit'
    if level_number < 10:
        d2head = 'MAP0' + str(level_number)
    else:
        d2head = 'MAP' + str(level_number)
    return d2head
