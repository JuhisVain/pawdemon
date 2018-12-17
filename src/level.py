import math


class Level:
    def __init__(self, level_number):
        self.number = level_number
        self.abstract_sectors = []

    def add_sector(self, abstract_sector):
        self.abstract_sectors.append(abstract_sector)

    def to_binary(self):
        return  # to be called by project at compilation
