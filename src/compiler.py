import struct
from functools import reduce

def compile_map(mapheader, vertices, things, sectors, sidedefs, linedefs,
                rejects, blockmaps, ssectors, segs, nodes):

    # The directory:
    #   8-byte string
    #   ???offset in 8-bits???
    #   ???size in 8-bits???
    
    directory_buffer = bytearray(0)
    
    with open('test', 'w+b') as testfile:
        testfile.write(bytes('PWAD    test1234', 'utf-8'))  # that's 16 bytes
        cur_offset = 16

        # The map's label should not need the shorts set to zero here:
        directory_buffer += mapheader.to_binary() + struct.pack('<HH', 0, 0)

        things_lump = reduce(lambda x, y : x + y, list(map(lambda x : x.to_binary(), things)))
        things_lump_size = len(things_lump)
        testfile.write(things_lump)
        directory_buffer += struct.pack('<8s', bytes('THINGS', 'utf-8'))
        directory_buffer += struct.pack('<HH', cur_offset, things_lump_size)
        cur_offset += things_lump_size

        testfile.write(directory_buffer) #  testing now -> Seems OK
