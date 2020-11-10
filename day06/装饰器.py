"""
1、什么是装饰器？
   器指的是工具，可以定义成函数
   装饰指的是为其他事务添加额外的东西点缀
   合并解释：
      即定义一个函数/类等 ，该函数是用来为其他函数添加额外的功能

2、为何要用装饰器？
    开放封闭原则
        开放：指的是对拓展功能是开放的
        封闭：指的对修改源代码是封闭的
    装饰器就是在不修改被装饰对象源代码以及调用方式前提下为被装饰对象添加新功能

3、如何用？
"""
# 方案一，修改了源代码
# import time
# def index(x,y):
#     start=time.time()
#     time.sleep(3)
#     print('index %s %s '%(x,y))
#     stop=time.time()
#     print(stop-start)
#
# index(111,222)

# 方案二，满足条件，但是代码冗余
# import time
# def index(x,y):
#     print('index %s %s '%(x,y))
#
# start=time.time()
# time.sleep(3)
# index(111,222)
# stop=time.time()
# print(stop-start)

# 方案三:调用方式改了
# import time

# def index(x, y):
#     time.sleep(3)
#     print('index %s %s ' % (x, y))
#
# def wrapper():
#     start = time.time()
#     index(111, 222)
#     stop = time.time()
#     print(stop - start)

# 方案三的优化:调用方式改了
# import time
#
# def index(x, y):
#     time.sleep(3)
#     print('index %s %s ' % (x, y))
#
# def wrapper(*args,**kwargs):
#     start = time.time()
#     index(*args,**kwargs)
#     stop = time.time()
#     print(stop - start)
# import time


# 方案四：在优化一的基础上把装饰对象写活了
# import time
#
#
# def index(x, y):
#     time.sleep(3)
#     print('index %s %s ' % (x, y))
#
# def home(name):
#     time.sleep(2)
#     print('welcome %s'%name)
#
# def outter(func):
#     # func=index
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         func(*args,**kwargs)
#         stop = time.time()
#         print(stop-start)
#     return wrapper
#
# index=outter(index) # index=outter(index的内存地址)
# index(111,222)
# home=outter(home) # home=outter(home的内存地址)
# home('sss')

# 方案五：模拟返回值
# import time
#
# def home(name):
#     time.sleep(2)
#     print('welcome %s'%name)
#     return 123
#
# def outter(func):
#     # func=index
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         res=func(*args,**kwargs)
#         stop = time.time()
#         print(stop-start)
#         return res
#     return wrapper
#
# home=outter(home) # home=outter(home的内存地址)
# res=home('sss')
# print(res)

# 语法糖：在被装饰对象正上方的单独一行写@装饰器名字
# 叠加多个装饰器，从下往上运行
# import time
#
# def outter(func):
#     # func=index
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         res=func(*args,**kwargs)
#         stop = time.time()
#         print(stop-start)
#         return res
#     return wrapper
# @outter # home=outter(home)
# def home(name):
#     time.sleep(2)
#     print('welcome %s'%name)
#     return 123
#
# home('hh')
#总结：无参装饰器模板
# def outter(func):
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         return res
#     return wrapper

from functools import wraps
def outter(func):
    @wraps(func) #将func的特性赋给wraps
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wrapper

@outter
def index(x, y):
    """这个是注释"""
    print(x,y)

index(1,2)
