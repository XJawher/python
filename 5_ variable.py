# variable
from __future__ import print_function

globalVariable = 100


def localAndGlovbleVariable():
    global globalVariable
    globalVariable = globalVariable + 100
    print('这是全局变量 globalVariable = ')
    print(globalVariable)
    localVariable = 10
    print('这是局部变量 localVariable = ')
    print(localVariable)


print(globalVariable)

localAndGlovbleVariable()
