if __name__ == '__main__':
    import re
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    fields = re.split(r'[;,\s]\s*', line)
    print(f'line split by multi char: {fields}')

    fields = re.split(r'(;|,|\s)\s*', line)
    print(f'line split by group match', fields)
    values = fields[::2]
    delimiters = fields[1::2]
    print(f'values of split: {values}\ndelimiters: {delimiters}')
