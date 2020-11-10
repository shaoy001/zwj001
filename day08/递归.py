"""
今日内容：
    一、叠加多个装饰器的加载、运行分析（了解）

    二、生成器的高级玩法之yield挂起函数：yield的表达式形式（了解）
    x=yield 返回值

    三、三元表达式

    四、生成式
       列表生成式
       字典生成式
       生成器表达式

    五、函数的递归调用

    六、二分法

"""

def deco1(func1):
    def wraper1(*args,**kwargs):
        print('第一个装饰器的wrapper')
        res1= func1(*args,**kwargs)
    return wraper1

def deco2(func2): #func2= wrapper3的内存地址
    def wraper2(*args,**kwargs):
        print('第二个装饰器的wrapper')
        res2= func2(*args,**kwargs)
    return wraper2
def deco3(x):
    def outter3(func3):
        def wraper3(*args,**kwargs):
            print('第三个装饰器的wrapper：%s'%x)
            res3= func3(*args,**kwargs)
        return wraper3
    return outter3

#加载顺序自下而上
# @deco1 #index = deco1(wrapper2的内存地址)==>index=wrapper1的内存地址
# @deco2 #index = deco2(wrapper3的内存地址)==>index=wrapper2的内存地址
# @deco3(111)# outter3>>index==outter3(index)==>>index=wrapper3的内存地址
# def index(x,y):
#     print('from index %s:%s'%(x,y))

# 执行顺序：自上而下执行
# index(1,2)

# yield挂起函数
# def dog(name):
#     food_list=[]
#     print('道哥%s准备吃东西啦...'%name)
#     while True:
#         x = yield food_list
#         print('道哥%s吃了%s'%(name,x))
#         food_list.append(x)
#
#
# g=dog('alex')
# res = g.send(None)# 等同于next(g)
# print(res)
# res1 =g.send('一根骨头')
# print(res1)
# g.send('肉包子')
# next(g)
# next(g)
# print(res1)

#三元表达式:格式：条件成立时返回if左边的值，不成立时返回右边值
x=1
y=2
res = x if x>y else y
print(res)
def func(x, y):
    if x==y:
        return 1
    else:
        return 2

# 列表生成式
l=['alex_dsb','lxx_dsb','wxx_dsb']
new_l=[]
new_l1=[]
for name in l:
    if name.endswith('dsb'):
        new_l.append(name)
# print(new_l)
# new_l = [name for name in l if name.endswith('dsb')]
new_l = [name for name in l if 1]
print(new_l)
new_l = [name.upper() for name in l]

#字典生成式
keys=['name','age','gender']
dic={key:None for key in keys}
print(dic)
items=[('name','egon'),('age',18),('gender','male')]
res={k:v for k,v in items if k!='gender'}
print(res)

#集合生成式
keys=['name','age','gender']
set={key for key in keys}
print(set)

#元祖生成式
g=(i for i in range(10) if i>3) #此刻g内部一个值也没有！！
print(g,type(g))
print(next(g))

with open('递归.py',mode='rt',encoding='utf-8') as f:
    # 方式一
    # res=0
    # for line in f:
    #     res+=len(line)
    # print(res)
    # 方式二
    # res=sum([len(line) for line in f])
    # print(res)
    # 方式三:效率最高，生成器，内存只有一个值
    # res=sum((len(line) for line in f))
    res = sum(len(line) for line in f)
    print(res)

#函数的递归调用：是函数嵌套调用的一种特殊形式
#具体是指：
#       在调用一个函数的过程中又直接或间接地调用到本身
#直接掉
# def f1():
#     print('是我是我还是我')
#     f1()
# f1()
#间接调用
# def f1():
#     print('调用f2')
#     f2()
# def f2():
#     print('调用f1')
#     f1()
# f1()
n=1
while n<10:
    n+=1
    print(n)
def f1(n):
    if n<10:
        n += 1
        print(n)
        f1(n)
f1(1)
#递归的两个阶段：回溯和递推
#回溯：一层一层调用下去
#递推：满足某种结束条件，结束递归调用，然后一层一层返回
#递归应用：
l=[1,2,[3,[4,[5,[6,[7,[8,[9]]]]]]]]
def f1(list1):
   for x in list1:
       if type(x) is list:
           f1(x)
       else:
           print(x)
f1(l)

