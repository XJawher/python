from __future__ import print_function


class getNumberData:
    name = 'number Calculator'
    defaultNumber = 20

    def add(self, x, y):
        print(x + y)

    def minus(self, x, y):
        print(x - y)

    def printSelf(self):
        print(self)


getNumberData = getNumberData()

print(getNumberData.name)
print(getNumberData.defaultNumber)
getNumberData.add(10, 20)
getNumberData.minus(30, 10)
getNumberData.printSelf()
