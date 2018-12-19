import struct
from project import Project, summon_header
from mapheader import Mapheader
from functools import reduce


def compile_project(project):
    # a PWAD will start with 'PWAD' followed by:
    # 32-bit int:  number of lumps
    # 32-bit int: location of directory

    lump_buffer = bytearray(0)
    directory_buffer = bytearray(0)
    
    lump_buffer += (bytes('PWAD', 'utf-8') + struct.pack('<II',  0, 0x0))
    #                                          WARNING!          ^  ^^^
    # that's 12 bytes
    cur_offset = 12

    for level in project.levels:
        level_data = level.gather_data()
        compile_map(Mapheader(summon_header(level_data[0], project.doom_version)),
                    level_data[1], level_data[4], level_data[2], level_data[3])



def compile_map(mapheader, vertices, things, sectors, sidedefs, linedefs):

    # The directory:
    #   offset in 8-bits
    #   size in 8-bits
    #   8-byte string
    
    directory_buffer = bytearray(0)
    
    with open('test', 'w+b') as testfile:
        testfile.write(bytes('PWAD', 'utf-8') + struct.pack('<II',  6, 0x1B4))
        #                                         WARNING!         ^^  ^^^^^

        # that's 12 bytes
        cur_offset = 12

        # The map's label should not need the shorts set to zero here:
        directory_buffer += struct.pack('<II', 0, 0) + mapheader.to_binary()

        # THINGS:
        things_lump = form_lump(things)
        things_lump_size = len(things_lump)
        testfile.write(things_lump)
        directory_buffer += struct.pack('<II', cur_offset, things_lump_size)
        directory_buffer += struct.pack('<8s', bytes('THINGS', 'utf-8'))
        cur_offset += things_lump_size

        # LINEDEFS:
        linedefs_lump = form_lump(linedefs)
        linedefs_lump_size = len(linedefs_lump)
        testfile.write(linedefs_lump)
        directory_buffer += struct.pack('<II', cur_offset, linedefs_lump_size)
        directory_buffer += struct.pack('<8s', bytes('LINEDEFS', 'utf-8'))
        cur_offset += linedefs_lump_size

        # SIDEDEFS
        sidedefs_lump = form_lump(sidedefs)
        sidedefs_lump_size = len(sidedefs_lump)
        testfile.write(sidedefs_lump)
        directory_buffer += struct.pack('<II', cur_offset, sidedefs_lump_size)
        directory_buffer += struct.pack('<8s', bytes('SIDEDEFS', 'utf-8'))
        cur_offset += sidedefs_lump_size

        # VERTEXES
        vertexes_lump = form_lump(vertices)  # olololo
        vertexes_lump_size = len(vertexes_lump)
        testfile.write(vertexes_lump)
        directory_buffer += struct.pack('<II', cur_offset, vertexes_lump_size)
        directory_buffer += struct.pack('<8s', bytes('VERTEXES', 'utf-8'))
        cur_offset += vertexes_lump_size

        # SECTORS
        sectors_lump = form_lump(sectors)
        sectors_lump_size = len(sectors_lump)
        testfile.write(sectors_lump)
        directory_buffer += struct.pack('<II', cur_offset, sectors_lump_size)
        directory_buffer += struct.pack('<8s', bytes('SECTORS', 'utf-8'))
        cur_offset += sectors_lump_size

        # write directory:
        testfile.write(directory_buffer)


def form_lump(lumplist):
    return reduce(lambda x, y: x + y, list(map(lambda x: x.to_binary(), lumplist)))
