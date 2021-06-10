if __name__ == '__main__':


    from itertools import dropwhile
    with open('/etc/passwd') as f:
        for line in dropwhile(lambda line: line.startswith('#'), f):
            print(line)

    from itertools import islice
    a = ['a', 'b', 'c', 'd', 1, 4, 10, 15]
    for x in islice(a, 3, None):
        print(x)