# print('Python was started in 1989 by "Guido".')
# print('Python was started in \'1989\' by \"Guido".')
#
#
# print(u'''静夜思
#
# 窗前明月光，
# 疑是地上霜，
# 举头望明月，
# 低头思故乡.''')

# print(1+2+3)
# print(7.5/2+12)
# print(1.0+2.0)
# print(11/4)
# print(11%4)
# print(2.5+10/4)


# 初始化一个集合使用［ ］来表示一个集合
# a=['zhansan','li','wangwu','zhaoliu']
# print(a)

# a =['Adam',95.5,'Lisa',85,'Bart',59]
# print(a)


# 集合添加元素（append insert）
# append()
# a=['zhansan','li','wangwu','zhaoliu']
# a.append("maqi")
# print(a)

#  insert()
# a=['zhansan','li','wangwu','zhaoliu']
# a.insert(0,"maqi")
# print(a)


# 删除集合中的元素
# 删除集合元素使用pop（）remove()
# pop()删除的操作是根据元素的位置及集合的下标进行删除操作
# remove() 删除的操作是根据元素来进行删除的操作
# a=['zhansan','li','wangwu','zhaoliu',"maqo"]
# a.pop()
# a.remove("maqo")
# print(a)

# L = ['Adam', 'Lisa', 'Paul', 'Bart']
# L.pop(-1)
# L.pop(-2)
# print(L)

# 对不为空的集合中的元素进行修改(根据指定位置来给元素进行重新的赋值)
# L = ['Adam', 'Lisa', 'Paul', 'Bart']
# L[-2]="Json"
# print(L)

# 在python中集合的创建有两种方法，list；tuple
# 相同点：a.都是便是一个集合;B.都可使用元素角标获取指定位置元素
# 不同点：a.创建的方法不一样，list创建使用［］表示，tuple使用()表示；b.list创建之后，可对元素进行增加，删除，修改等操作，而tuple不能
# b=('zhangsan',"lisi","wangwu","zhaoliu")
# print(b[2])
# print(b)

# if循环语句  if之后添加判断，且以：结尾及表示判断语句开始执行

# a=11
# if a>=18:
#     print("above 18")
# else:
#     print("below 18")

# 当遇到多重判断时，使用if...elif...elif...elif....else
# 如果按照分数划定结果：

# 90分或以上：excellent
# 80分或以上：good
# 60分或以上：passed
# 60分以下：failed

# example
# score=89
# if score>=90:
#     print("excellent")
# elif score>=80:
#     print("good")
# elif score>=60:
#     print("passed")
# else:
#     print("failed")

# for循环遍历集合
# L = [75, 92, 59, 68]
# sum=0.0
#
# for s in L:
#     sum=sum+s
# print(sum/4)

# while循环（求100之内奇数和）
# sum=0.0
# x=1
# while x <100:
#     sum=sum+x
#     x=x+2
# print(sum)

# 在循环遍历时，结束循环使用关键字break
# 利用 while True 无限循环配合 break 语句，计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。
# sum=0.0
# x=1
# n=1
# while True:
#     sum=sum+x
#     x=x*2
#     n=n+1
#     if n>20:
#         break
# print(sum)

# 遍历集合时，想跳过某一次循环使用关键字continue
# 对已有的计算 0 - 100 的while循环进行改造，通过增加 continue 语句，使得只计算奇数的和：
# sum=0.0
# x=0
# while True:
#    x=x+1
#    if x>100:
#        break
#    if x%2==0:
#        continue
#
#    sum=sum+x
# print(sum)

# 多重循环：for嵌套for

# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
#         if x < y:
#             print (x * 10 + y)


# 涉及到集合，除了list tuple之外，现在还有类似于java中的map，涉及到key－value，dict就是python中的map
# 1.dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。
# 2.dict的第二个特点就是存储的key-value序对是没有顺序的！
# 3.dict的第三个特点是作为 key 的元素必须不可变
#   'Adam' ==> 95
#   'Lisa' ==> 85
#   'Bart' ==> 59
# d={
#     "Adam":95,
#     "Lisa":85,
#     "Brat":59
# }
# d.__setitem__("zhangsan",20)
# print(d)

# 获取dict中某一个value
# d = {
#     'Adam': 95,
#     'Lisa': 85,
#     'Bart': 59
# }
# print(d)

# 获取集合中元素(遍历集合)
# for di in d:
#     print(d[di])


# set集合就相当于一个去重的效果，可以结合list，tuple使用，避免元素重复,set存储的是无序集合

# s=set(['a','b','c','c','c','d'])
# print(s)

# set的元素是tuple

# s=set([('zhangsan',20),('lisi',30),("wangwu",12)])
# for x in s:
#     print(x[0],'age is:',x[1])

#set进行元素的更新，一是添加新的元素到set集合中，二是将已有的元素移除
# s=set([1,2,4,5,6,7,8])
# s.add(9)
# print(s)
# s.remove(1)
# print(s)

# example:
# 针对下面的set，给定一个list，对list中的每一个元素，如果在set中，就将其删除，如果不在set中，就添加进去。
# s = set(['Adam', 'Lisa', 'Paul'])
# L = ['Adam', 'Lisa', 'Bart', 'Paul']
# s = set(['Adam', 'Lisa', 'Paul'])
# L = ['Adam', 'Lisa', 'Bart', 'Paul']
#
# for name in L:
#     if name in s:
#         s.remove(name)
#     else:
#         s.add(name)
# print(s)

# 函数
# abs绝对值 str将指定参数转换成字符串

# print(abs(-1))
# print(abs(2))
# print(abs(1.1))
# print(str(123))

# L=[]
# x=1
# while x <= 100:
#     L.append(x*x)
#     x=x+1
# print(sum(L))


# def square_of_sum(L):
#     sum = 0
#     for x in L:
#         sum=sum+x*x
#     return sum
# L=[1,2,3,4,5,6,7,8,9]
# print(square_of_sum(L))

# 定义函数，且函数的入参是包含默认值
# def greet(name='world'):
#
#     print('hello,'+name+'.')
#
# greet()
# greet('zhnagsna')

# 对于指定方法的入参的个数不一定，则可使用可变参来定义

# def sum(*args):
#     sum=0.0
#     if len(args)==0:
#         return sum
#     else:
#         for x in args:
#             sum=sum+x
#         return sum
#
# print(sum())
# print(sum(1,3,4,5.6))

#对list进行切片，及在从原来集合切出指定的集合 tuple同样可以进行同样的处理
# [a:b:c] a代表的是起始位置，b代表的是截止位置，c代表的是去元素的间隔 也可以进行倒序切片
# L=[1,2,3,4,5,6,7,8,9]
# print(L[:])
# print(L[:3])
# print(L[::3])
# print(L[-3:])
# S=(2,3,4,5,6,5)
# print(S[:])
# print(S[:3])

# 字符串的切片
# s='123456'
# print(s[::2])

# 索引迭代适应关键字enumerate来实现对list的迭代,该关键字实现的是将list的索引和索引对应的值转换成tuple，list中包含多个tuple例如：
# example
# L=['zhangsan','lisa','wangwu','zhaoliu']
#
# for index,name in enumerate(L):
#     print(index,'-',name)

# dict的遍历  values（） itervalues() items()
# d={
#     'lisa':20,
#     'zhangsan':12,
#     'wangwu':33
# }
# for k in d.values():
#     print(k)
# for k in d.__iter__():
#     print(k)
# for k ,v in d.items():
#     print(k,'-',v)

# x=1
#
# for x in range(1,100,2):
#     print(x*(x+1))

# print([x*(x+1) for x in range(1,100,2)])

# 多层表达式
print([100*n1+10*n2+n3 for n1 in range(1,10) for n2 in range(1,10) for n3 in range(1,10) if n1==n3])
