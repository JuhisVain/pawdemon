import struct

import thing
import sidedef


def main():
    my_thing = sidedef.Sidedef(1, 2, "12345678", "test", "abcdefg", 666)
    with open('test', 'w+b') as testfile:
        testfile.write(my_thing.to_binary())
    
    


if __name__ == "__main__":
    main()
