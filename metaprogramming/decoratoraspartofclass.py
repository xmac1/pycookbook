from functools import wraps

class A:
    def decortor1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("decorator 1")
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("decorator 2")
            return func(*args, **kwargs)
        return wrapper


if __name__ == '__main__':
    a = A()

    @a.decortor1
    def add(x, y):
        return x + y

    @A.decorator2
    def sub(x, y):
        return x - y

    add(1, 2)
    sub(1, 2)