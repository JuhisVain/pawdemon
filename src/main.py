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
from level import Level

import tool


def main():

    vrts = [Vertex(64,64), Vertex(64,192), Vertex(192,192), Vertex(192,64)]
    as1 = Absec(vrts[0], vrts[1], vrts[2])
    as1.add_vertex(vrts[3], vrts[2], vrts[0])

    lev1 = Level(2, 1)
    lev1.add_sector(as1)


#   maph = mapheader.Mapheader("MAP01")  # doom 2
#
#   vert0 = vertex.Vertex(64, 64)
#   vert1 = vertex.Vertex(64, 192)
#   vert2 = vertex.Vertex(192, 192)
#   vert3 = vertex.Vertex(192, 64)

#   vert4 = vertex.Vertex(320, 192)
#   vert5 = vertex.Vertex(320, 64)

#   playerstart = thing.Thing(96, 96, 0, 1, 7)  # flip on first 3 bits of options just in case

#   sect0 = sector.Sector(0, 256, 'FLOOR0_1', 'FLOOR0_3', 150, 0, 0)

#   sect1 = sector.Sector(10, 196, 'FLOOR0_1', 'FLOOR0_3', 100, 0, 0)

#   sidef0 = sidedef.Sidedef(0, 0, 'CEMENT1', 'CEMENT1', 'CEMENT1', 0)
#   sidef1 = sidedef.Sidedef(0, 0, 'CEMENT2', 'CEMENT2', 'CEMENT2', 0)
#   sidef2 = sidedef.Sidedef(0, 0, 'CEMENT3', 'CEMENT3', '-', 0)  # middle texture goes at end
#   sidef3 = sidedef.Sidedef(0, 0, 'CEMENT4', 'CEMENT4', 'CEMENT4', 0)

#   sidef4 = sidedef.Sidedef(0,0,'CEMENT1', 'CEMENT1', 'CEMENT1', 1)
#   sidef5 = sidedef.Sidedef(0,0,'CEMENT1', 'CEMENT1', 'CEMENT1', 1)
#   sidef6 = sidedef.Sidedef(0,0,'CEMENT1', 'CEMENT1', 'CEMENT1', 1)
#   sidef7 = sidedef.Sidedef(0,0,'-', '-', '-', 1)

#   lidef0 = linedef.Linedef(0, 1, 0, 0, 0, 0, 0xffff)
#   lidef1 = linedef.Linedef(1, 2, 0, 0, 0, 1, 0xffff)
#   lidef2 = linedef.Linedef(2, 3, 4, 0, 0, 2, 7)  # two sided,0,0,2, rightside sidedef
#   lidef3 = linedef.Linedef(3, 0, 0, 0, 0, 3, 0xffff)

#   lidef4 = linedef.Linedef(2,4,0,0,0,4,0xffff)
#   lidef5 = linedef.Linedef(4,5,0,0,0,5,0xffff)
#   lidef6 = linedef.Linedef(5,3,0,0,0,6,0xffff)

#   compiler.compile_map(maph,
#                        [vert0,vert1,vert2,vert3,vert4,vert5],
#                        [playerstart],
#                        [sect0, sect1],
#                        [sidef0,sidef1,sidef2,sidef3,sidef4,sidef5,sidef6,sidef7],
#                        [lidef0,lidef1,lidef2,lidef3,lidef4,lidef5,lidef6])
                         #[rej],
                         #[blmap],
                         #[ssec0], #,ssec1],
                         #[seg0,seg1,seg2,seg3],
                         #[node0])

if __name__ == "__main__":
    main()
