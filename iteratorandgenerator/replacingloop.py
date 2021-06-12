if __name__ == '__main__':
    import sys
    f = open('/etc/passwd')
    for chunk in iter(lambda: f.read(10), b''):
        sys.stdout.write(chunk)