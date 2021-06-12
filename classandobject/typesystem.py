class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        print(f'check type')
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {self.expected_type}')
        super().__set__(instance, value)


class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected > 0')
        super(Unsigned, self).__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError("missing size options")
        super(MaxSized, self).__init__(name, **opts)

    def __set__(self, instance, value):
        if value >= self.size:
            raise ValueError(f'value must be < {self.size}')
        super(MaxSized, self).__set__(instance, value)


class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    pass

class Float(Typed):
    expected_type = float


class UnsignedFloat(Unsigned, Float):
    pass


class String(Typed):
    expected_type = str


class SizedString(MaxSized, String):
    pass


class checkmeta:
    def __new__(cls, clsname, bases, methods):
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return super(checkmeta, self).__new__(cls, clsname, bases, methods)


class Stock(metaclass=checkmeta):
    name = SizedString( size=8)
    shares = UnsignedInteger()
    stock = UnsignedFloat()

    def __init__(self, name, shares, stock):
        self.name = name
        self.shares = shares
        self.stock = stock