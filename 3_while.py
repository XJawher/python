from __future__ import print_function
condition = 0


def loopOfWhile(condition):
    while condition:
        print(condition, end=' ')
        condition = condition - 1


condition = 10
loopOfWhile(condition)
