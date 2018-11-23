import struct

import thing
import sidedef
import vertex

import tool


def main():
    #my_thing = sidedef.Sidedef(1, 2, "12345678", "test", "abcdefg", 666)
    #with open('test', 'w+b') as testfile:
    #    testfile.write(my_thing.to_binary())

    #print(tool.seg_distance(1, 1, 2, 2))
    #print(tool.seg_distance(0, 0, 2, 2))
    #print(tool.seg_distance(2, 2, 1, 1))
    #print(tool.seg_distance(2, 2, 0, 0))

    lv = vertex.Vertex(10, 10)
    sv = vertex.Vertex(10, 5)

    print(tool.seg_angle(lv.x, lv.y, sv.x, sv.y))


    
    


if __name__ == "__main__":
    main()
