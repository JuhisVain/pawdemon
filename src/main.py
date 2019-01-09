import struct

import thing
import sidedef
import linedef
from vertex import Vertex
import reject
import blockmap
import mapheader
import sector
import ssector
import seg
import node
import compiler

from abstract_sector import Abstract_sector as Absec
from project import Project
from level import Level

import tool


def main():

    testpro = Project(2)
    
    vrts = [Vertex(64,64), Vertex(64,192), Vertex(192,192), Vertex(192,64)]
    as1 = Absec(vrts[0], vrts[1], vrts[2])
    as1.add_thing(thing.Thing(96, 96, 0, 1, 7))
    as1.add_vertex(vrts[3], vrts[2], vrts[0])

    #as1.set_linedef_flag(2, )

    lev1 = testpro.add_level_by_num(1)
    lev1.add_sector(as1)

    vrts = [Vertex(64,192), Vertex(64,500), Vertex(300,500), Vertex(192,192)]
    as1 = Absec(vrts[0], vrts[1], vrts[2])
    as1.add_vertex(vrts[3], vrts[2], vrts[0])

    lev1.add_sector(as1)

    testpro.compile()


if __name__ == "__main__":
    main()
