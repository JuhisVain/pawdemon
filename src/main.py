import struct

import thing
import sidedef
import vertex
import reject
import blockmap

import tool


def main():
    #my_thing = sidedef.Sidedef(1, 2, "12345678", "test", "abcdefg", 666)
    #with open('test', 'w+b') as testfile:
    #    testfile.write(my_thing.to_binary())

    #tr = reject.Reject(231)
    #with open('test', 'w+b') as testfile:
    #    testfile.write(tr.to_binary())

    bl = blockmap.Blockmap(1, 2, 3, 2)
    bl.blocklistlist = [[1,2,5], [6,7,8,10], [1,3,5,7,9], [2,4], [0,11,12], [3,2,1,0]]

    with open('test', 'w+b') as testfile:
        testfile.write(bl.to_binary())

if __name__ == "__main__":
    main()
