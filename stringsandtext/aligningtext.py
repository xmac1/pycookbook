if __name__ == '__main__':
    text = 'Hello World'
    print(f'left just string: "{text.ljust(20)}"')
    print(f'right just string: "{text.rjust(20)}"')
    print(f'center just string: "{text.center(20)}"')

    print(f'right align format: "{format(text, ">20")}"')
    print(f'left align format: "{format(text, "<20")}"')
    print(f'center align format: "{format(text, "^20")}"')

    print(f'format with align character: "{format(text, "*^20s")}"')
    print(f'format multiple string: "{"{:>10s} {:>10s}".format("hello", "world")}"')
