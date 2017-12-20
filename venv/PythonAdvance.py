#                       Python 进阶学习和代码练习

# 函数式编程
# 针对的都是计算，Python是一门高级的编程语言


# 高阶函数：
# 在Python中变量可以指向函数，而变量可以作为函数的参数，这样函数可以作为另一个函数的入参

# example
import math

def add(x,y,f):
    return f(x)+f(y)

print(add(4,9,math.sqrt))