from __future__ import print_function
# from 5_variabe import localAndGlovbleVariable
from test import localAndGlovbleVariable


class getNumberData:
    name = 'number Calculator'
    defaultNumber = 20

    def add(self, x, y):
        print(x + y)

    def minus(self, x, y):
        print(x - y)

    def printSelf(self):
        print(self)


# getNumberData = getNumberData()

# print(getNumberData.name)
# print(getNumberData.defaultNumber)
# getNumberData.add(10, 20)
# getNumberData.minus(30, 10)
# getNumberData.printSelf()


class inheritGetNumberData(getNumberData):
    # print(getNumberData)
    pass


# inheritGetNumberData = inheritGetNumberData()
# inheritGetNumberData.add(20, 30)
# print(inheritGetNumberData)

localAndGlovbleVariable()

