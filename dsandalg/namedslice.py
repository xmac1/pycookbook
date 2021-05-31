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

    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]

    from operator import itemgetter
    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    print(f"sort by fname: {rows_by_fname}")
    print(f'sort by uid: {rows_by_uid}')

    class User:
        def __init__(self, user_id):
            self.user_id = user_id

        def __repr__(self):
            return f'User({self.user_id})'


    users = [User(23), User(9), User(99)]
    from operator import attrgetter
    users = sorted(users, key=attrgetter('user_id'))
    print(f'sort users by user_id: {users}')

    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]

    rows.sort(key=itemgetter('date'))
    from itertools import groupby
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print('    ', i)

    from collections import defaultdict
    rows_by_date = defaultdict(list)
    for row in rows:
        rows_by_date[row['date']].append(row)

    for r in rows_by_date:
        print(r)
        for i in rows_by_date[r]:
            print('    ', i)