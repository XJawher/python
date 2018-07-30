##Python-缩进
在 Python 中缩进是非常重要的一个常规知识点,必须要完整的掌握好缩进的关系,这样才能完善的进行 Python 的开发工作.
不能有空格的地方:
1. 冒号后面不能有空格

必须有空格的地方:
1. 函数名前必须要有空格
2. 关键字后面必须要有空格
3. 参数和运算符前后都要有空格

必须有换行的地方:
`expected 2 blank lines after class or function definition, found 1`
在函数和类后面必须要有两行作为换行符

[python 基础语法range](https://docs.pythontab.com/python/python2.7/controlflow.html#range)
##Python- if and else


```
def test(number):
    if number > 100:
        print 'number is > 100'
    elif number < 100 and number > 50:
        print '50 < number < 100 '
    else:
        print 'number < 50 '
    if number:
        print number


test(60)

```
在 if 和 else 中,需要注意的是 **elif** 这个和 JS 的不一样,比较的特殊.在判断中 == 才是判断是否相等的条件.
## Python- 三目运算
在 JS 中有个三目运算 condition ? value1 : value2,是非常的方便的一个简短处理返回值的方法.在 Python 中,这样的简短处理的方案就是 `var = var1 if condition else var2`
## Python- for
在 Python 中 for 循环是和 JS 中的有非常大的区别的.先看一下一个最简单的例子

```
def ForFunctionForList(list):
    for element in list:
        print(element)


ForFunctionForList([1, 2, 3, 4, 5, 6])
# 1, 2, 3, 4, 5, 6
```
在 Python 中可以被 for 循环的有 **列表、字符串、元组** 而在 JS 中字符串是无法被 for 循环直接循环的,但是在 Python 中,却是可以做 for 循环的,这是很奇特的一个知识点
```
def ForFunctionForString(string):
    for element in string:
        print(element, end=' ')


ForFunctionForString('hello')

```
先来接收一个新的知识点: Tuple ,元组 (xxx,yyy,zzz),元组也是可以被循环的,
```
def ForLoopForTuple(Tuple):
    for element in Tuple:
        print(element, len(element), end=' ')


ForLoopForTuple(('n', 'hao', 'ya'))

```
字典,也就是 JS 中的对象, dictionary, 也是可以被循环的,而且循环的时候类似于 ES6 中的 Object.entries 或者说是 JS 抄的 py 的也说不准,管他呢,用着爽就是了,注意在这个字典的循环中 key 是乱序的

```
from __future__ import print_function


def forFunctionToDict(dict):
    for key in dict:
        print(key, dict[key], end=' ')


dict = {}
dict['lan'] = 'python'
dict['version'] = '2.7'
dict['platform'] = '64'

forFunctionToDict(dict) # platform 64 lan python version 2.7 

```
而对于 set 数据,同样的也是可以进行循环,在循环的时候 set 有个特点就是会去重,和上面的字典一样的,在循环的时候输出是乱序的
```
def forFunctionToSet(set):
    for elements in set:
        print(elements, end=' ')


setDataStructure = set(['python', 'python2', 'python3', 'python'])
forFunctionToSet(setDataStructure)

```
在上面的字典和 set 中,输出全部是乱序的,如果我们想要输出一个有序的该怎么输出才对呢?
##Python_variable
Python 的变量要比 JS 的简单太多了, JS 中的变量有7个基本的类型,这7种变量类型中,有四个是非引用类型,两个是引用类型有一个是 ES6 中新增的类型, string,undefined,number,boolean,function,obj,symble,而且在变量声明的时候需要用 let 或者 const 做声明.否则就是一个会报错的无效的变量,然而在 py 中变量是不用这么声明的直接赋值就是了,暂时不清楚是不是存在作用域的问题,需要进一步的探索和研究.
在 py 中可以同时定义多个变量比如像这样
`a,b,c=11,12,13`
##Python_while 循环
while 循环中的基础的概念和 JS 循环是一致的,在循环中通过 condition 来判断是不是继续循环或者直接 break 跳出循环
```
from __future__ import print_function
condition = 0


def loopOfWhile(condition):
    while condition < 10:
        print(condition, end=' ')
        condition = condition + 1


loopOfWhile(condition)

```
在 while 中, condition 比较除了比较常规的 < > <= >= == != 这些返回 true 和 fales 之外,当 condition 值为数字的时候,并且当数字大于0时是为 true,condition 为 none 时返回 false,condition 为集合类型的数据, list dict tuple set 时候当他们的元素不为 0 时返回 true, 当为 0  的时候返回 false
##Python_函数 参数
在函数参数这里分为可变的参数或者不变参数,

```
def report(name, *grades):
    total_grade = 0
    for grade in grades:
        total_grade += grade
    print(name, 'total grade is ', total_grade)
```

### 可变参数 *

在上面的代码中 *grades 就是把第一个参数后面的所有的参数都给做成一个集合,就是类似 ES6 中的 ... 一样,只不过在 Python 中 *grades 的属性是 tuple 也就是元组,而在 ES6 中 ... 的属性是数组,这就是不同的地方,不过是类似的,概念是相通的.

###关键字参数 **

在关键字参数中前面是有两个 ** 号,而在可变参数中却是一个 * 号.
可变参数和关键字参数的不同之处就在于可变参数是会把传入的参数变成一个元组也就是 tuple 而关键字参数会把值变成一个 dictionary 也就是字典, JS 中的 object,
```
# keyword parameter
from __future__ import print_function


def keywordParameter(name, **keywordParameter):
    print('name is', name)
    for (key, word) in keywordParameter.items():
        print(key, word, end=' ')


keywordParameter('Mike', age=24, country='China', education='bachelor')

```
在字典的循环中记得和 JS 不同的地方是 **keywordParameter.items()** 这是不一样的地方.