# class A:
#     __x=1
#     def __init__(self,name):
#         self.__nam=name
#     def __foo(self):
#         print('run foo')
#     def bar(self):
#         self.__foo()
#         print('from bar')
#
# a=A('egon')
# # print(a.__name)
# print(a._A__x)
# print(a._A__name)
# #print(a.__x)
# a.bar()
"""
1、外部无法直接obj.__AttrName
2、在类内部obj.__AttrName
3、子类无法覆盖父类__开头的属性
4、变形的过程只在类定义阶段发生（类扩展属性时无效）
5、可以构造只调自己类里面的方法
"""
#封装数据属性：明确的区分内外,控制外部对隐藏的属性的操作行为
class People:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def tell_info(self):
        print('Name:<%s> Age:<%s>'%(self.__name,self.__age))

p=People('egon',18)
p.tell_info()
print(p._People__name)
#封装方法：隔离复杂度
class ATM:
    def __card(self):
        print('插卡')
    def __auth(self):
        print('用户认证')
    def __input(self):
        print('输入取款金额')
    def __print_bill(self):
        print('打印账单')
    def __take_money(self):
        print('取款')

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()

a=ATM()
a.withdraw()
# property
class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight = weight
        self.height=height
    @property #调用执行并返回时，不用加括号，让调用者以为调用的是个属性
    def bmi(self):
        return self.weight/(self.height**2)

p=People('Ayden',62,1.7)
# p.bmi=p.weight/(p.height**2)
# print(p.bmi())
# p1=People('zwj',50,1.55)
# # # p1.bmi=p1.weight/(p1.height**2)
# # print(p1.bmi())
# print(p.bmi)
# print(p1.bmi)
# 绑定方法与非绑定方法
"""
在类内部定义的函数，分为两大类：
一：绑定方法：绑定给谁，就应该由谁来调用，谁来调用就会把调用者当作第一个参数自动传入
    绑定到对象的方法：在类内定义的没有被任何装饰器修饰的
    绑定到类的方法:在类内部定义的被装饰器classmethod修饰的方法(即便是对象调用，类也会当作第一个参数自动传入)
二：非绑定方法：没有自动传值这么一说,就是类中定义的一个普通工具
    不与类或者对象绑定
"""
# class Foo:
#     def __init__(self,name):
#         self.name=name
#     def tell(self):
#         print('名字是%s'%self.name)
#         return 1
#
#     @classmethod
#     def func(cls):
#         print(cls)
#         return 1
#     @staticmethod
#     def func1(x,y):#不会传其他值
#         return x+y
#
# f=Foo('egon')
# # print(f)
# # print(Foo.tell(f))
# # f.tell()
# # print(f.tell())
# f.func()
# print(Foo.func())
# print(Foo.func1(3,4))
# print(f.func1(2,3))
#
# import hashlib
# import time
# dict1={'name':'Ayden','Age':28,'sex':'male'}
# class People:
#     def __init__(self,name,age,sex):
#         self.id=self.create_id()
#         self.name=name
#         self.age=age
#         self.sex=sex
#
#     def tell_info(self):#绑定到对象的方法
#         print('Name:%s Age:%s Sex:%s'%(self.name,self.age,self.sex))
#     @classmethod
#     def from_conf(cls):
#         obj=cls(
#             dict1['name'],
#             dict1['Age'],
#             dict1['sex']
#         )
#         return obj
#     @staticmethod
#     def create_id():
#         m=hashlib.md5(str(time.time()).encode('utf-8'))
#         return m.hexdigest()
#
# p1=People('egon',18,'male')
# #绑定给对象，就应该由对象来调用，自动将对象本身当作第一个参数传入
# p1.tell_info()#tell_info(p1)
#
# #绑定给类，就应该由类来调用，自动将类本身当作第一个参数传入
# p2=People.from_conf()#from_conf(People)
# p2.tell_info()
#
# #非绑定方法，不与类或者对象绑定，谁都可以调用，没有自动传值一说
# print(p1.create_id())

#反射：通过字符串映射到对象的属性
# class People:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def talk(self):
#         print('%s is talking'%self.name)
#
# obj=People('egon',18)
# #.后面一定是属性，而不是字符串
# print(obj.name)
# print(obj.talk)
# obj.talk()
# #choice=input('>>:')#choice='name'
# #print(obj.choice)#print(obj.'name')
# #判断有没有
# print(hasattr(obj,'name'))
# print(hasattr(obj,'talk'))
# choice1=input('>>:')#choice='name'
# #获取
# print(getattr(obj,choice1))#print(obj.'name')
# print(getattr(obj,'ddd',None))#print(obj.'name')
# #设置
# setattr(obj,'sex','male')#obj.sex='male'
# print(obj.sex)
# #删除
# delattr(obj,'sex')#del obj.sex
# print(obj.sex)

#反射的应用
class Service:
    def run(self):
        while True:
            inp=input('>>:').strip()#cmd ='get a.txt'
            cmds=inp.split()#cmds=['get','a.txt']
            if hasattr(self,cmds[0]):
                func=getattr(self,cmds[0])
                func(cmds)
    def get(self,cmds):
        print('get.......',cmds)

    def put(self,cmds):
        print('put.......',cmds)

obj=Service()
obj.run()