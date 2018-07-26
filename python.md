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