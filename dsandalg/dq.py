from collections import deque

if __name__ == '__main__':
    q = deque(maxlen=3)
    q.append(1)
    q.append(2)
    q.append(3)
    print(f'append 1 2 3, {q}')
    q.append(4)
    print(f'append 4, {q}')
    q.append(5)
    print(f'append 5, {q}')