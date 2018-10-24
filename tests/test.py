import filecmp
import hashlib
import json

import mate


def mate_to_json():
    """
    Tests reading of mate file and exports data as a json file
    """
    data = mate.read_mate("assets/5000000000.mate")

    print("Saving file output/5000000000.mate.json...")
    with open("output/5000000000.mate.json", "w+") as outfile:
        out_obj = []
        for entry in data:
            out_obj.append(entry.__dict__)

        outfile.write(json.dumps(out_obj, indent=4, separators=(',', ': ')))


def mate_to_binary_string():
    """
    Tests that data is recompiled correctly and matches the original file
    """
    data = mate.read_mate("assets/5000000000.mate")
    binary_data = mate.compile_mate(data)

    hash_md5 = hashlib.md5()
    with open("assets/5000000000.mate", "rb") as infile:
        for chunk in iter(lambda: infile.read(4096), b""):
            hash_md5.update(chunk)

    file_hash = hash_md5.hexdigest()

    hash_md5 = hashlib.md5()
    pos = 0
    for chunk in iter(lambda: binary_data[pos:pos + 4096], b""):
        pos += 4096
        hash_md5.update(chunk)

    string_hash = hash_md5.hexdigest()

    print("The file and binary string are the same: {0}".format(file_hash == string_hash))


def mate_to_binary_file():
    """
    Tests reading data from mate file then writes the same data back as a binary
    """
    data = mate.read_mate("assets/5000000000.mate")
    mate.write_mate(data, "output/5000000000.mate")
    print("The files are the same: {0}".format(filecmp.cmp("assets/5000000000.mate", "output/5000000000.mate")))


def main():
    mate_to_json()
    mate_to_binary_string()
    mate_to_binary_file()


if __name__ == "__main__":
    main()
