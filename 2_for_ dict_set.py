from __future__ import print_function


def forFunctionToDict(dict):
    for key in dict:
        print(key, dict[key], end=' ')


dict = {}
dict['lan'] = 'python'
dict['version'] = '2.7'
dict['platform'] = '64'

# forFunctionToDict(dict)


def forFunctionToSet(set):
    for elements in set:
        print(elements, end=' ')


setDataStructure = set(['python', 'python2', 'python3', 'python'])
forFunctionToSet(setDataStructure)
