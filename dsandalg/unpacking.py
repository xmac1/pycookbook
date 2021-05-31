from statistics import mean

def drop_first_last(grades):
    first, *middle, last = grades
    return mean(middle)


if __name__ == '__main__':
    s = 'Hello'
    a, b, c, d, e = s
    print(f'a:{a}, b:{b}, c:{c}, d:{d}, e:{e}')

    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    _, shares, price, _ = data
    print(f'shares: {shares}')

    m = drop_first_last([10, 5, 8, 7, 9])
    print(f'average grade: {m}')

    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    name, email, *phones = record
    print('name')