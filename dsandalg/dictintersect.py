if __name__ == '__main__':
    a = {
        'x': 1,
        'y': 2,
        'z': 3,
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2,
    }

    print(f'relative complement of b in a, {a.keys() - b.keys()}')