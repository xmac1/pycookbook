if __name__ == '__main__':
    x = 1234.56789
    print(f'two decimal places of accuracy: "{format(x, "0.2f")}"')
    print(f'right justified in 10 char, one-digit accuracy: "{format(x, ">10.1f")}"')
    print(f'include thousands separator: "{format(x, ",.1f")}"')
    print(f'use exponential notation: "{format(x, "0.2e")}"')