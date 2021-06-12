class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        val = self.func(instance)
        setattr(instance, self.func.__name__, val)
        return val

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        return 2 * math.pi * self.radius
    