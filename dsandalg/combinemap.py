if __name__ == '__main__':
    from collections import ChainMap

    a = {'x': 1, 'z': 2}
    b = {'y': 3, 'z': 4}
    c = ChainMap(a, b)
    for k, v in c.items():
        print(f'key: {k}, value: {v}')