import json
import sys
import os.path


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as file_handle:
        loaded_data = json.loads(file_handle.read(), strict=False)
    return loaded_data


def pretty_print_json(loaded_data):
    print(json.dumps(loaded_data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if os.path.exists(filename):
            try:
                loaded_data = load_data(filename)
            except ValueError as err:
                print('Error parsing JSON:', err)
            else:
                pretty_print_json(loaded_data)
        else:
            print("Error: File " + filename + " doesn't exist")
    else:
        print('Error: filename is not specified')
