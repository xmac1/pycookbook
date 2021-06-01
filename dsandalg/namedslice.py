if __name__ == '__main__':
    record = '....................100          .......513.25     ..........'

    SHARES = slice(20, 32)
    PRICE = slice(40, 48)

    cost = int(record[SHARES]) * float(record[PRICE])
    print(f'cost: {cost}')

    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]

    from collections import Counter
    counter = Counter(words)
    top_three = counter.most_common(3)
    print(f'top three words: {top_three}')

