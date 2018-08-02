# list
from __future__ import print_function

# list.append(obj) 对列表进行扩展

exampleList = [1, 234, 5, 6, 'a', 'b', 'a', 'a']


def listAppend(example):
    listAppendOflist = example
    listAppendOflist.append('a')
    print(listAppendOflist)  # 他会去同步的改变 exampleList 或者说是修改他的指针


listAppend(exampleList)


def listCount(example):
    print(example.count('a'))


listCount(exampleList)


def listExtend(aList, bList):
    aList.extend(bList)
    print(aList)


aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2009, 'manni']
listExtend(aList, bList)


def listIndex(example):
    print(example.index('a'))


listIndex(exampleList)


def listRemove(example):
    example.remove('a')
    print(example)
    print(exampleList)


listRemove(exampleList)


def listPop(example):
    print(example.pop(1))
    print(example)


listPop(exampleList)


def listReverse(example):
    example.reverse()
    print(example)


listReverse(exampleList)


def listSort(example):
    example.sort()
    print(example)


listSort(exampleList)

def listInsert(example):
    
