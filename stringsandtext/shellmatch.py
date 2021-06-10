if __name__ == '__main__':
    from fnmatch import fnmatch, fnmatchcase
    print(f'"foo.txt" match "*.txt"? {fnmatch("foo.txt", "*.txt")}')
    name = 'foo.txt'
    pattern = '?oo.txt'
    print(f'"{name}" match "{pattern}"? {fnmatch(name, pattern)}')

    patterns = 'Dat*.csv'
    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    print(f'files match "{patterns}": {[name for name in names if fnmatch(name, patterns)]}')