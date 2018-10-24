import json
import os

import mate


def main():
    data = mate.read_mate(r"C:\botw-data\decompressed\content\Terrain\A\MainField\5000000000.mate.stera\5000000000.mate")

    with open('output/5000000000.mate.json', 'w+') as outfile:
        out_obj = []
        for entry in data:
            out_obj.append(entry.__dict__)

        outfile.write(json.dumps(out_obj, indent=4, separators=(',', ': ')))


if __name__ == "__main__":
    main()
