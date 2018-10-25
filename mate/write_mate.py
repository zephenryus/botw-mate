import struct


def write_mate(data: list, outfile_name: str) -> None:
    if len(data) != 65536:
        if len(data) < 65536:
            print("Error 2001: Data list is not long enough. Expected 65536 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 65536 but saw {}".format(len(data)))
        exit(2002)

    with open(outfile_name, 'wb+') as outfile:
        binary_data = compile_mate(data)
        outfile.write(binary_data)


def compile_mate(data: list) -> bytes:
    if len(data) != 65536:
        if len(data) < 65536:
            print("Error 2001: Data list is not long enough. Expected 65536 but saw {}".format(len(data)))
            exit(2001)

        print("Error 2002: Data list is too long. Expected 65536 but saw {}".format(len(data)))
        exit(2002)

    mate_binary = b''
    for index in range(65536):
        blend_weight = int((data[index].blend_weight * 255)) & 255
        mate_binary += struct.pack('>4B', data[index].material_0_index, data[index].material_1_index, blend_weight,
                                   data[index].unknown)

    return mate_binary
