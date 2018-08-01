from __future__ import print_function
# from 5_variabe import localAndGlovbleVariable
# from test import localAndGlovbleVariable


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


class testInit:
    # print(getNumberData)
    className = 'testInit'
    price = 19

    def __init__(self, name, price, height, width, weight):
        self.name = name
        self.price = price
        self.height = height
        self.width = width
        self.weight = weight


testInit = testInit('bad calculator', 18, 17, 16, 15)

print(testInit.name)
print(testInit.price)
print(testInit.height)
print(testInit.width)
print(testInit.weight)

# inheritGetNumberData = inheritGetNumberData()
# inheritGetNumberData.add(20, 30)
# print(inheritGetNumberData)

# localAndGlovbleVariable()
