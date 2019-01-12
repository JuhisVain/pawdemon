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
    lev1 = testpro.add_level_by_num(1)

    asec = Absec(Vertex(0,0),Vertex(0,200),Vertex(200,200))
    asec.add_vertex(Vertex(200,0),Vertex(200,200),Vertex(0,0))
    asec.add_thing(thing.Thing(96, 96, 0, 1, 7))
    lev1.add_sector(asec)

    asec = Absec(Vertex(0,200),Vertex(0,400),Vertex(200,400))
    asec.add_vertex(Vertex(200,200),Vertex(200,400),Vertex(0,200))
    lev1.add_sector(asec)

    asec = Absec(Vertex(200,400),Vertex(400,400),Vertex(400,200))
    asec.add_vertex(Vertex(200,200),Vertex(400,200),Vertex(200,400))
    lev1.add_sector(asec)
    
    asec = Absec(Vertex(200,0),Vertex(200,200),Vertex(400,200))
    asec.add_vertex(Vertex(400,0),Vertex(400,200),Vertex(200,0))
    lev1.add_sector(asec)

    testpro.compile()


if __name__ == "__main__":
    main()
