if __name__ == '__main__':
    a = [1, 2, 3, 4]
    for x in reversed(a):
        print(x)

    class Countdown:
        def __init__(self, start):
            self.start = start

        def __iter__(self):
            n = self.start
            while n > 0:
                yield n
                n -= 1

        def __reversed__(self):
            n = 1
            while n <= self.start:
                yield n
                n += 1

    forward = list(Countdown(5))
    reverse = list(reversed(Countdown(5)))
    print(f'forward: {forward}, reversed: {reverse}')