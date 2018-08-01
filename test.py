# variable
from __future__ import print_function

globalVariable = 100


def localAndGlovbleVariable():
    global globalVariable
    globalVariable = globalVariable + 100
    print('globalVariable = ')
    print(globalVariable)
    localVariable = 10
    print(' localVariable = ')
    print(localVariable)


print(globalVariable)

# localAndGlovbleVariable()
print(__name__)
