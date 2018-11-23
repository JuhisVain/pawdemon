import struct

import thing
import sidedef
import vertex
import reject

import tool


def main():
    #my_thing = sidedef.Sidedef(1, 2, "12345678", "test", "abcdefg", 666)
    #with open('test', 'w+b') as testfile:
    #    testfile.write(my_thing.to_binary())

    tr = reject.Reject(231)
    with open('test', 'w+b') as testfile:
        testfile.write(tr.to_binary())

if __name__ == "__main__":
    main()
