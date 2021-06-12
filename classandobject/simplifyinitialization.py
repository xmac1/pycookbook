class Structure:
    _fields = []
    def __init__(self, *args):
        if len(*args) > len(self._fields):
            raise TypeError

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    class Point(Structure):
        _fields = ['x', 'y']

    class Circle(Structure):
        _fields = ['radius']

    s = Stock('ACME', 50, 90.1)
    p = Point(1, 2)
    c = Circle(1.0)