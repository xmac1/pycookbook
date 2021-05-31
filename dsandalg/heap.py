import heapq

if __name__ == '__main__':
    nums = [1, 4, 0, 23, 543, -52, 2, 5, 23, -1]
    hp = list(nums)
    heapq.heapify(hp)
    print(f'heap: {hp}')
    print(f'heap pop: {heapq.heappop(hp)}')
    

