# 先定义类
class LuffyStudent:
    school='luffycity' #数据属性
    def learn(self): #函数属性
        print('is learning')
    def eat(self):
        print('is eating')
    def sleep(self):
        print('is sleeping')
        return 1

# 后产生对象
# stu1=LuffyStudent()
# stu2=LuffyStudent()
# stu3=LuffyStudent()
# print(stu1.sleep())

# 查看类的名称空间
print(LuffyStudent.__dict__)
print(LuffyStudent.__dict__['school'])
print(LuffyStudent.__dict__['sleep'])
#查
print(LuffyStudent.school)
print(LuffyStudent.sleep)
#增
LuffyStudent.county='China'
print(LuffyStudent.county)
# 删
# del LuffyStudent.sleep
# print(LuffyStudent.sleep)
# 改
LuffyStudent.county='China11'
print(LuffyStudent.county)
# 类的数据属性是公用一份，类的函数属性，是绑定给对象使用的
# 对象的调用绑定方法时，会把对象本身当作第一个参数传入，传给self
#面向对象小结:可扩展性强
class Chinese:
    country='China'
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def eat(self):
        print('%s is eating!'%self.name)

p1=Chinese('egon',18,'male')
p2=Chinese('alex',38,'female')
p3=Chinese('wpq',48,'female')

print(p1.country)
p1.eat()
p2.eat()
p3.eat()
class Student:
    school='luffycity'
    count=0
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        Student.count+=1

    def learn(self):
        print('%s is learning'%self.name)

stu1=Student('egon',18,'male')
print(stu1.count)
stu2=Student('alex',38,'female')
print(stu1.count)
stu3=Student('wpq',48,'female')
print(stu1.count)
print(Student.count)
# 继承
# class Garen:
#     camp='Demacia'
#
#     def __init__(self,nickname,life_value,aggresicity):
#         self.nickname=nickname
#         self.life_value=life_value
#         self.aggresicity=aggresicity
#
#     def attack(self,enemy):
#         enemy.life_value-=self.aggresicity
#
#
# class Riven:
#     camp = 'Noxus'
#
#     def __init__(self, nickname, life_value, aggresicity):
#         self.nickname = nickname
#         self.life_value = life_value
#         self.aggresicity = aggresicity
#
#     def attack(self, enemy):
#         enemy.life_value -= self.aggresicity
#
# g1=Garen('草丛伦',100,20)
# r1=Riven('可爱的瑞文',80,50)
# g1.attack(r1)
# print(r1.life_value)

class Hero:
    def __init__(self, nickname, life_value, aggresicity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresicity = aggresicity

    def attack(self, enemy):
        enemy.life_value -= self.aggresicity

class Garen(Hero):
    life_value=30
class Riven(Hero):
    pass

g1=Garen('草丛伦',100,20)
r1=Riven('可爱的瑞文',80,50)
g1.attack(r1)
print(r1.life_value)
# 先去父类中找，再去自己类中找
# print(g1.life_value)
# # 派生：
# class Hero:
#     camp = 'None'
#     def __init__(self, nickname, life_value, aggresicity):
#         self.nickname = nickname
#         self.life_value = life_value
#         self.aggresicity = aggresicity
#
#     def attack(self, enemy):
#         enemy.life_value -= self.aggresicity
#
# class Garen(Hero):
#     camp='Demacia'
# class Riven(Hero):
#     camp = 'Noxus'
# g1=Garen('草丛伦',100,20)
# r1=Riven('可爱的瑞文',80,50)
# g1.attack(r1)
# print(r1.life_value)
# print(r1.camp)
# 在python3中，只有新式类：一个类没有继承object类，默认也会继承
# 经典类会按照深度优先的方式查找下去
# 新式类会按照广度优先的方式查找下去
# foo.mro()可以查看类的调用顺序（新式类有此方法）
class foo:
    pass
class foo1():
    pass
class foo2(object):
    pass
print(foo.__bases__,foo1.__bases__,foo2.__bases__)
#在子类中重用父类的属性
#方式一：指名道姓
#方式二：super（依赖继承）
class Hero:
    camp = 'None'
    def __init__(self, nickname, life_value, aggresicity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresicity = aggresicity

    def attack(self, enemy):
        enemy.life_value -= self.aggresicity

# class Garen(Hero):
#     camp='Demacia'
#     def __init__(self,nickname, life_value, aggresicity,weapon):
#         # self.nickname = nickname
#         # self.life_value = life_value
#         # self.aggresicity = aggresicity
#         Hero.__init__(self,nickname, life_value, aggresicity)
#         self.weapon=weapon
#     def attack(self, enemy):
#         Hero.attack(self, enemy)#指名道姓
#         print('from Garen Class')
#
# g1=Garen('草丛伦',100,20)
# r1=Riven('可爱的瑞文',80,50)
# g1.attack(r1)
# print(r1.life_value)
class Garen(Hero):
    camp='Demacia'
    def __init__(self,nickname, life_value, aggresicity,weapon):
    #     # self.nickname = nickname
    #     # self.life_value = life_value
    #     # self.aggresicity = aggresicity
    #     Hero.__init__(self,nickname, life_value, aggresicity)
        super().__init__(nickname, life_value, aggresicity)
        self.weapon=weapon
    def attack(self, enemy):
        super().attack(enemy)#依赖继承
        # Hero.attack(self, enemy)#指名道姓
        print('from Garen Class')

g1=Garen('草丛伦',100,20,'hha')
r1=Riven('可爱的瑞文',80,50)
g1.attack(r1)
print(r1.life_value)
# 组合：
#类.属性名=另一个实例化类的对象
# 抽象类与归一化,子类必须使用父类的方法
import abc
class Animal(metaclass=abc.ABCMeta):#这个抽象类只能被继承，不能被实例化
    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def eat(self):
        pass

class People(Animal):
    def run(self):
        pass
    def eat(self):
        pass
    pass

p1=People()
#多态：同一类事物的多种形态
#多态性：指的是可以在不考虑对象的类型的情况下而直接使用对象
