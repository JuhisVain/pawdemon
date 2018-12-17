import struct
from functools import reduce

def compile_project(project):
    # The 'PWAD'+2 ints should be written here
    # mapcar compilemap on project's level list or whatever python does
    # where to calc lump counts and file pointers?

def compile_map(mapheader, vertices, things, sectors, sidedefs, linedefs):
                #rejects, blockmaps, ssectors, segs, nodes):

    # a PWAD will start with PWAD followed by:
    # 32-bit int:  number of lumps
    # 32-bit int: location of directory

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

        # SEGS
#       segs_lump = form_lump(segs)
#       segs_lump_size = len(segs_lump)
#       testfile.write(segs_lump)
#       directory_buffer += struct.pack('<II', cur_offset, segs_lump_size)
#       directory_buffer += struct.pack('<8s', bytes('SEGS', 'utf-8'))
#       cur_offset += segs_lump_size

        # SSECTORS
#       ssectors_lump = form_lump(ssectors)
#       ssectors_lump_size = len(ssectors_lump)
#       testfile.write(ssectors_lump)
#       directory_buffer += struct.pack('<II', cur_offset, ssectors_lump_size)
#       directory_buffer += struct.pack('<8s', bytes('SSECTORS', 'utf-8'))
#       cur_offset += ssectors_lump_size

        # NODES
#       nodes_lump = form_lump(nodes)
#       nodes_lump_size = len(nodes_lump)
#       testfile.write(nodes_lump)
#       directory_buffer += struct.pack('<II', cur_offset, nodes_lump_size)
#       directory_buffer += struct.pack('<8s', bytes('NODES', 'utf-8'))
#       cur_offset += nodes_lump_size

        # SECTORS
        sectors_lump = form_lump(sectors)
        sectors_lump_size = len(sectors_lump)
        testfile.write(sectors_lump)
        directory_buffer += struct.pack('<II', cur_offset, sectors_lump_size)
        directory_buffer += struct.pack('<8s', bytes('SECTORS', 'utf-8'))
        cur_offset += sectors_lump_size

        # REJECT
#       rejects_lump = form_lump(rejects)
#       rejects_lump_size = len(rejects_lump)
#       testfile.write(rejects_lump)
#       directory_buffer += struct.pack('<II', cur_offset, rejects_lump_size)
#       directory_buffer += struct.pack('<8s', bytes('REJECT', 'utf-8'))
#       cur_offset += rejects_lump_size

        # BLOCKMAP
#       blockmaps_lump = form_lump(blockmaps)
#       blockmaps_lump_size = len(blockmaps_lump)
#       testfile.write(blockmaps_lump)
#       directory_buffer += struct.pack('<II', cur_offset, blockmaps_lump_size)
#       directory_buffer += struct.pack('<8s', bytes('BLOCKMAP', 'utf-8'))
#       cur_offset += blockmaps_lump_size


#       testfile.write(bytearray(15))
        # write directory:
        testfile.write(directory_buffer)


def form_lump(lumplist):
    return reduce(lambda x, y: x + y, list(map(lambda x: x.to_binary(), lumplist)))
