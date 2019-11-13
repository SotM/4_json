import json


def load_data(filepath):
    file_handle = open(filepath, 'r', encoding='cp1251')
    loaded_data = file_handle.read()
    file_handle.close()

    try:
        json_data = json.loads(loaded_data, strict=False)
    except ValueError as err:
        print('Error parsing JSON:', err)
        json_data = ''

    return json_data


def pretty_print_json(input_shops_data):
    print(json.dumps(input_shops_data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    shops_data = load_data('shops.json')
    pretty_print_json(shops_data)
