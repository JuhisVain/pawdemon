import math

import compiler
from level import Level


class Project:
    def __init__(self, doom_version):
        self.doom_version = doom_version
        self.levels = []

    def add_level(self, level_number):
        self.levels.append(Level(level_number))

    def compile(self):
        compiler.compile_project(self)


# Do these belong here or in the compiler? ...
def summon_header(level_number, doom_version):
    if doom_version == 1:
        return doom1_head(level_number)
    elif doom_version == 2:
        return doom2_head(level_number)
    else:
        print("Ding dong")
        return doom2_head(level_number)


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
