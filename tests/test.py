import json

import mate


def mate_to_json():
    """
    Tests reading of mate file and exports data as a json file
    """
    data = mate.read_mate(r"assets/5000000000.mate")

    with open('output/5000000000.mate.json', 'w+') as outfile:
        out_obj = []
        for entry in data:
            out_obj.append(entry.__dict__)

        outfile.write(json.dumps(out_obj, indent=4, separators=(',', ': ')))


def main():
    mate_to_json()


if __name__ == "__main__":
    main()
