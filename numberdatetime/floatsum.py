if __name__ == '__main__':
    import math
    nums = [1.23e18, 1, -1.23e18]
    print(f'sum of {nums}: {sum(nums)}')
    print(f'float sum of {nums}: {math.fsum(nums)}')