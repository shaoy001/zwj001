# 有参装饰器
# def auth(db_type):
#     def deco(func):
#         def wrapper(*args,**kwargs):
#             name = input("请输入你的名字：").strip()
#             pwd = input("请输入你的密码：").strip()
#             if db_type == '1':
#                 if name == 'egon' and pwd == '123':
#                     res=func(*args,**kwargs)
#                     return res
#             if db_type == '2':
#                 pass
#             else:
#                 print('user or password error')
#         return wrapper
#     return deco
#
# @auth('file') #
# def index(x,y):
#     print(x,y)

#有参装饰器模板
# def 有参装饰器(x,y,z):
#     def outter(func):
#         def wrapper(*args,**kwargs):
#             res = func(*args,**kwargs)
#             return res
#         return wrapper
#     return outter
#
# @有参装饰器(1,y=2,z=3)
# def 被装饰对象():
#     pass
"""
1、什么是迭代器
    迭代器指的是迭代取值的工具，迭代式一个重复的过程，每次重复都是
    基于上一次的结果而继续的，单纯的重复并不是迭代

2、为何要有迭代
    迭代器是用来迭代取值的工具，而涉及到把多个值循环
    取出来的类有：列表、字符串、元祖、字典、集合、打开文件

    上述迭代取值的方式只适用于有索引的数据类型：
    列表、字符串、元祖
    为了解决这个问题，故产生了迭代器

3、如何用迭代器
但凡内置有__iter__方法的都称之为可迭代对象

"""
# 3、可迭代对象与迭代器对象详解
# 可迭代对象：内置有__iter__方法
#   可迭代对象.__iter__()：得到迭代器对象
# 迭代器对象：内置有__next__方法并且内置有__iter__方法
#     迭代器对象.__next__()：得到迭代器的下一个值
#     迭代器对象.__iter__()：得到迭代器本身，说白了和没调一样
#for循环的工作原理
d={'a':1,'b':2,'c':3}
#1、d.__iter__()得到一个迭代器对象
#2、迭代器对象.__next__()拿到一个返回值，然后将该值返回给k
#3、循环往复步骤2，直到抛出StopIteration异常for循环会捕捉异常然后结束训选
for k in d:
    print(k)
#list('hello') #原理同for循环
# 迭代器优缺点总结
# 优点：1、惰性计算，每个时间点在内存中只有一个值，只有在需要时才会调用next
#2、为序列和非序列提供了一种统一的迭代取值方式
#缺点：1、除非取尽，否则无法获得迭代器长度
#2、只能取下一个值，不能回到开始

#生成器：自定义生成器
# 在函数内一旦存在yield关键字，调用函数并不会执行函数体代码
# 会返回一个生成器对象，生成器即自定义的迭代器

def func():
    print('第一次')
    yield 1
    print('第二次')
    yield 2
    print('第三次')
    yield 3

g=func()
print(g)
g.__iter__()
g.__next__()
g.__next__()
g.__next__()

# 会触发函数体代码的运行，然后遇到yield停下来，
# 将yield后的值当作本次调用结果的返回

# 应用管理
def my_range(start,stop,step=1):
    print('start....')
    while start<stop:
        yield start
        start+=step
    print('end....')

g=my_range(1,5,2)
print(next(g))
print(next(g))

for n in my_range(1,7,2):
    print(n)