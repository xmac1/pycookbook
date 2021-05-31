from collections import OrderedDict

if __name__ == '__main__':
    d = OrderedDict()
    d['foo'] = 2
    d['bar'] = 1
    d['spam'] = 3
    d['grok'] = 4
    for key in d:
        print(f'{key}: {d[key]}')