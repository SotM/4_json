import json


def load_data(filepath):
    # fin = open(filepath, 'r', encoding='utf8')
    fin = open(filepath, 'r', encoding='cp1251')
    loaded_data = fin.read()
    fin.close()

    try:
        data = json.loads(loaded_data, strict=False)
    except ValueError as err:
        print('Error:', err)
        data = ''
    except:
        data = ''
    else:
        print('ok')

    return data


def pretty_print_json(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    shops_data = load_data('shops.json')
    pretty_print_json(shops_data)
