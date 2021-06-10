if __name__ == '__main__':
    s = '{name} has {n} messages.'
    print(s.format(name='Guido', n=37))
    name = 'Guido'
    n = 37
    print(f'use format_map and vars: "{s.format_map(vars())}"')

    class Info:
        def __init__(self, name, n):
            self.name = name
            self.n = n

    a = Info('Guido', 37)
    print(f'use vars with class: "{s.format_map(vars(a))}"')

    class safesub(dict):
        def __missing__(self, key):
            return '{' + key + '}'

    del n
    print(f'deal with missing keys: "{s.format_map(safesub(vars()))}"')

    import sys

    def sub(text):
        return text.format_map(safesub(sys._getframe(1).f_locals))

    name = "Guido"
    n = 37
    print(f'frame hack: {sub("Hello, {name}")}')
    print(f'frame hack: {sub("Your favorite color is {color}")}')