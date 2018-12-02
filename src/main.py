import struct

import thing
import sidedef
import linedef
import vertex
import reject
import blockmap
import mapheader
import sector
import ssector
import seg
import node
import compiler

import tool


def main():
    #my_thing = sidedef.Sidedef(1, 2, "12345678", "test", "abcdefg", 666)
    #with open('test', 'w+b') as testfile:
    #    testfile.write(my_thing.to_binary())

    #tr = reject.Reject(231)
    #with open('test', 'w+b') as testfile:
    #    testfile.write(tr.to_binary())

    #bl = blockmap.Blockmap(1, 2, 3, 2)
    #bl.blocklistlist = [[1,2,5], [6,7,8,10], [1,3,5,7,9], [2,4], [0,11,12], [3,2,1,0]]

    #maph = mapheader.Mapheader("E1M1")
    
    #with open('test', 'w+b') as testfile:
    #    testfile.write(maph.to_binary())

    # let's try to manually create a level:

    maph = mapheader.Mapheader("MAP01")  # doom 2
    
    vert0 = vertex.Vertex(64, 64)
    vert1 = vertex.Vertex(64, 192)
    vert2 = vertex.Vertex(192, 192)
    vert3 = vertex.Vertex(192, 64)

    playerstart = thing.Thing(96, 96, 0, 1, 7)  # flip on first 3 bits of options just in case

    sect0 = sector.Sector(0, 256, 'FLOOR0_1', 'FLOOR0_3', 150, 0, 0)

    sidef0 = sidedef.Sidedef(0, 0, 'CEMENT1', 'CEMENT1', 'CEMENT1', 0)
    sidef1 = sidedef.Sidedef(0, 0, 'CEMENT2', 'CEMENT2', 'CEMENT2', 0)
    sidef2 = sidedef.Sidedef(0, 0, 'CEMENT3', 'CEMENT3', 'CEMENT3', 0)
    sidef3 = sidedef.Sidedef(0, 0, 'CEMENT4', 'CEMENT4', 'CEMENT4', 0)

    lidef0 = linedef.Linedef(0, 1, 0, 0, 0, 0, 0xffff)
    lidef1 = linedef.Linedef(1, 2, 0, 0, 0, 1, 0xffff)
    lidef2 = linedef.Linedef(2, 3, 0, 0, 0, 2, 0xffff)
    lidef3 = linedef.Linedef(3, 0, 0, 0, 0, 3, 0xffff)

    rej = reject.Reject(1)

    blmap = blockmap.Blockmap(0, 0, 2, 2)
    blmap.blocklistlist = [[0,3],[3,2],[1,0],[2,1]]

    #  That's the simple stuff...

    ssec0 = ssector.Ssector(4, 0)
    #ssec1 = ssector.Ssector(0, 4)
    
    seg0 = seg.Seg(0,1, 16384, 0, 0, 0)
    seg1 = seg.Seg(1,2, 0, 1, 0, 0)
    seg2 = seg.Seg(2,3, 0x8000, 2, 0, 0)
    seg3 = seg.Seg(3,0, 0xc000, 3, 0, 0)

    node0 = node.Node(64,64, 0,128, 256,0,0,256, 0,0,0,0, 0xc000 + 0, 0xc000 + 1)

    compiler.compile_map(maph,
                         [vert0,vert1,vert2,vert3],
                         [playerstart],
                         [sect0],
                         [sidef0,sidef1,sidef2,sidef3],
                         [lidef0,lidef1,lidef2,lidef3],
                         [rej],
                         [blmap],
                         [ssec0], #,ssec1],
                         [seg0,seg1,seg2,seg3],
                         [node0])

if __name__ == "__main__":
    main()
