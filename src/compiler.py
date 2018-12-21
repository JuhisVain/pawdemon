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
    lump_count = 0

    for level in project.levels:
        level_data = level.gather_data()
        compiled_data = compile_map(Mapheader(summon_header(level_data[0],
                                                            project.doom_version)),
                                    level_data[1], level_data[5], level_data[3],
                                    level_data[4], level_data[2], cur_offset)
        lump_buffer += compiled_data[0]
        directory_buffer += compiled_data[1]
        cur_offset = compiled_data[2]
        lump_count += 6  # Currently so

    with open('test', 'w+b') as testfile:
        testfile.write(lump_buffer)
        testfile.write(directory_buffer)
        testfile.seek(4)
        testfile.write(struct.pack('<II', lump_count, len(lump_buffer)))


def compile_map(mapheader, vertices, things, sectors,
                sidedefs, linedefs, cur_offset):
    lump_buffer = bytearray(0)
    directory_buffer = bytearray(0)

    # The map's label should not need the shorts set to zero here:
    directory_buffer += struct.pack('<II', 0, 0) + mapheader.to_binary()

    # THINGS:
    things_lump = form_lump(things)
    things_lump_size = len(things_lump)
    lump_buffer += things_lump
    directory_buffer += struct.pack('<II', cur_offset, things_lump_size)
    directory_buffer += struct.pack('<8s', bytes('THINGS', 'utf-8'))
    cur_offset += things_lump_size

    # LINEDEFS:
    linedefs_lump = form_lump(linedefs)
    linedefs_lump_size = len(linedefs_lump)
    lump_buffer += linedefs_lump
    directory_buffer += struct.pack('<II', cur_offset, linedefs_lump_size)
    directory_buffer += struct.pack('<8s', bytes('LINEDEFS', 'utf-8'))
    cur_offset += linedefs_lump_size

    # SIDEDEFS
    sidedefs_lump = form_lump(sidedefs)
    sidedefs_lump_size = len(sidedefs_lump)
    lump_buffer += sidedefs_lump
    directory_buffer += struct.pack('<II', cur_offset, sidedefs_lump_size)
    directory_buffer += struct.pack('<8s', bytes('SIDEDEFS', 'utf-8'))
    cur_offset += sidedefs_lump_size

    # VERTEXES
    vertexes_lump = form_lump(vertices)  # olololo
    vertexes_lump_size = len(vertexes_lump)
    lump_buffer += vertexes_lump
    directory_buffer += struct.pack('<II', cur_offset, vertexes_lump_size)
    directory_buffer += struct.pack('<8s', bytes('VERTEXES', 'utf-8'))
    cur_offset += vertexes_lump_size

    # SECTORS
    sectors_lump = form_lump(sectors)
    sectors_lump_size = len(sectors_lump)
    lump_buffer += sectors_lump
    directory_buffer += struct.pack('<II', cur_offset, sectors_lump_size)
    directory_buffer += struct.pack('<8s', bytes('SECTORS', 'utf-8'))
    cur_offset += sectors_lump_size

    return [lump_buffer, directory_buffer, cur_offset]


def form_lump(lumplist):
    return reduce(lambda x, y: x + y, list(map(lambda x: x.to_binary(), lumplist)))
