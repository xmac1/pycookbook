if __name__ == '__main__':
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    p1 = {key: value for key, value in prices.items() if value > 100}
    print(f'items with price > 100: {p1}')

    from collections import namedtuple
    Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
    stock_prototype = Stock('', 0, 0, None, None)
    def dict_to_stocks(s):
        return stock_prototype._replace(**s)

    a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
    stock = dict_to_stocks(a)
    print(f'stock: {stock}')
    