if __name__ == '__main__':
    from datetime import datetime

    text = '2012-09-20'
    y = datetime.strptime(text, '%Y-%m-%d')
    z = datetime.now()
    diff = z - y
    print(f'delta of {y} and {z} is {diff.total_seconds()/3600:0.2f} hours')