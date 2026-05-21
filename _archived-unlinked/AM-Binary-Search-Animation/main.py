from random import randint
from time import sleep

SLEEP_AMT = 0.5


def binSearch(data, target, lo, hi):
    if lo > hi:
        print('Not found')
        return False

    print(data)
    mid = (lo + hi) // 2
    print('  ' + '    ' * mid + '^')
    sleep(SLEEP_AMT)

    if data[mid] == target:
        print('Found it')
        return True
    elif data[mid] > target:
        print('Too high\n')
        sleep(SLEEP_AMT)
        binSearch(data, target, lo, mid - 1)
    else:
        print('Too low\n')
        sleep(SLEEP_AMT)
        binSearch(data, target, mid + 1, hi)


data = sorted([randint(10, 99) for _ in range(10)])
key = data[6]
print('Searching for ' + str(key) + '\n')
binSearch(data, key, 0, 9)
