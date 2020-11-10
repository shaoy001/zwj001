#什么是异常：异常是错误发生的信号，一旦程序出错，并且程序没有处理这个错误，错误就会抛出异常，并且程序的运行随之终止
print('1')
print('2')
print('3')
# int('aaa')
# print('4')
# print('5')
# print('6')
#2、错误分为两种
#语法错误：在程序执行前就要立刻改正过来
#print('xxx'
# if 1>2
# 逻辑错误
# ValueError
# int('aaa')
#NameError
# name
#IndexError
# l=[1,2,3]
# l[100]
# KeyError
# d={'name':'lzy'}
# d['nae']

#AttributeError
# class Foo:
#     pass
#
# Foo.xxx
#TypeError
# for i in 3:
#     pass

#3、异常
# 强调一：对于错误发生的条件可以预知，此时应该用if判断去预防异常
# 强调二：对于错误发生的条件是不可以预知的，此时应该用try...except
# 多分支
try:
    print('1')
except NameError as e:
    print('====>',e)
except KeyError as e:
    print('=====>',e)
#万能异常，对所有异常均用同一判断时使用，也可与多分支结合使用
try:
    print('1')
except Exception as  e:
    print('异常发生啦',e)
else:
    print('在被检测的代码块中没有发生异常时执行')

finally:
    print('不管被监测的代码块有没有发生异常都执行')

#主动触发异常：raise 异常类型（值）
class People:
    def __init__(self,name,age):
        if not isinstance(name,str):
            raise TypeError('名字必须传入str类型')
        self.name=name
        self.age=age

p=People('egon', 18)

#其他结构
#自定义异常
class MyException(BaseException):
    def __init__(self,msg):
       super(MyException,self).__init__()
       self.msg=msg
    def __str__(self):
        return '<%s>'%self.msg

raise MyException('我自己的异常类型')



#assert
info={}
info['name']='egon'
info['age']=18
assert ('name' in info) and ('age' in info)
if info['name'] == 'egon' and info['age']>10:
    print('welcome')
