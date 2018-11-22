import struct

import thing


def main():
    my_thing = thing.Thing(1, 2, 45, 123, 234)
    with open('test', 'w+b') as testfile:
        testfile.write(my_thing.to_binary())
    
    


if __name__ == "__main__":
    main()
