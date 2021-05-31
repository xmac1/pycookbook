if __name__ == '__main__':
    nums = [1, 2, 4, 5, 6]
    s = sum(x ** 2 for x in nums)
    print(f'square sum: {s}')

    s = ('ACME', 50, 123.45)
    csv = ', '.join(str(c) for c in s)
    print(f'csv: {csv}')

