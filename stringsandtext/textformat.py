if __name__ == '__main__':
    import textwrap
    s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
        the eyes, not around the eyes, don't look around the eyes, \
        look into my eyes, you're under."

    print(textwrap.fill(s, 70))

    import os
    print(textwrap.fill(s, os.get_terminal_size().columns, initial_indent='  '))
