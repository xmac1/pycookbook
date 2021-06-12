if __name__ == '__main__':
    items = ['a', 'b', 'c']
    from itertools import permutations
    for p in permutations(items, 2):
        print(p)

    from itertools import combinations
    for c in combinations(items, 3):
        print(f'combinations: {c}')