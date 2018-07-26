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
在 if 和 else 中,需要注意的是 **elif** 这个和 JS 的不一样,比较的特殊.
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