if __name__ == '__main__':
    import io

    s = io.StringIO()
    n = s.write('Hello, World\n')
    print(f'write {n} to s: {s.getvalue()}')