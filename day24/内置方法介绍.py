# class Foo:
#     pass
# obj=Foo()
# #实例是否属于对象
# a=isinstance(obj,Foo)
# print(a)
# class Bar(Foo):
#     pass
# #对象是否是某对象的子对象
# b=issubclass(Bar,Foo)
# print(b)
# class Foo:
#     def __init__(self,name):
#         self.name=name
#     def __getitem__(self, item):
#         print('getitem...')
#         print(item)
#         return self.__dict__[item]
#     def __setitem__(self, key, value):
#         print('setitem...')
#         print(key,value)
#         self.__dict__[key]=value
#     def __delitem__(self, key):
#         print('setitem....')
#         print(key)
#         self.__dict__.pop(key)
#
# obj=Foo('egon')
# #obj.属性名
# print(obj['name'])
# #obj.sex='male'
# obj['sex']='male'
# print(obj.__dict__)
# del obj['name']
# print(obj.__dict__)
#
# d=dict({'name':'zwj'})
# print(d)
# class Foo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def __str__(self):
#         print('========>')
#         return '[name:%s,age:%s]'%(self.name,self.age)
#
# obj=Foo('egon',18)
# #自动返回__str__方法
# print(obj)
# f=open('a.txt')
# f.read()
# f.close()#回收操作系统资源
# print(f)
# class Open:
#     def __init__(self,filename):
#         print('open file....')
#         self.filename=filename
#     def __del__(self):
#         print('回收操作系统资源:self.close()')
#
#
# f=Open('a.txt')
# #del f#f.__del__()，在对象删除之前会调用该方法
# print('-----main----')

#元类:
#储备知识exec
#参数1：字符串形式的命令
#参数2：全局作用域(字典形式)，如果不指定默认就使用globals()
# print(globals())
# #参数3：局部作用域（字典形式），如果不指定默认就使用locals()
#
# g={
#     'x':1,
#     'y':2
# }
# l={}
# exec("""
# global x,m
# x=10
# m=100
# z=3
# """,g,l)
# print(g)
# print(l)

#一切皆对象，对象可以怎么用？
#1、都可以被引用，x=obj
#2、都可以当作函数的参数传入
#3、都可以当作函数的返回值
#4、都可以当作容器类的元素，l=[func,time,obj,1]
# class Foo:
#     pass
# obj=Foo()
# #产生类的类称之为元类，默认所有用class定义的类，他们的元类是type
# #定义类的两种方式
# class Chinese:
#     country='China'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def talk(self):
#         print('%s is talking'%self.name)
#
# #方式二：type
# class_name='Chinese'
# class_bases=(object,)
# class_body="""
# country='China'
# def __init__(self,name,age):
#     self.name=name
#     self.age=age
# def talk(self):
#     print('%s is talking'%self.name)
# """
# class_dict={}
# exec(class_body,globals(),class_dict)
# print(class_dict)
# Chinese1=type(class_name,class_bases,class_dict)

#知识储备__call__方法
class Foo:
    def __call__(self, *args, **kwargs):
        print(self)
        print(args)
        print(kwargs)
obj2=Foo()
obj2(1,2,3,a=1,b=2)
#自定义元类控制类
class Goo:
    pass
class Foo(object,metaclass=Goo):
    pass