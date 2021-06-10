import datetime

if __name__ == '__main__':
    from datetime import timedelta

    a = timedelta(days=1, hours=2, minutes=3)
    b = timedelta(hours=5)
    c = a + b
    print(f'{a} + {b} is: {c}, is equal to {c.seconds} seconds')

    a = datetime.datetime.now()
    delta = timedelta(days=1, hours=10)
    print(f'time after {delta} from now is {a + delta}')

    