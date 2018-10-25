import os
import struct

from .Mate import Mate


def read_mate(path: str, verbose=False) -> list:
    """
    Decompiles terrain material to a list of Mate objects

    :param path:        Path to .mate file to be decompiled
    :param verbose:     Print messages to console
    :return:            List of Mate objects
    """
    material_array = []

    if os.path.exists(path):
        if verbose:
            print("Reading {}...".format(path))

        with open(path, 'rb') as infile:
            # Each file contains 65,536 entries (256 * 256)
            for _ in range(65536):
                material_0_index, material_1_index, blend_weight, unknown = struct.unpack('<4B', infile.read(4))
                material_array.append(Mate(
                    material_0_index,
                    material_1_index,
                    blend_weight / 255,  # Normalize the weight value to a float between 0–1
                    unknown
                ))

    return material_array
