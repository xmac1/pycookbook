class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


if __name__ == '__main__':
    date = Date(1996, 3, 28)
