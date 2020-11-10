"""
面向过程：核心是过程二字，过程指的是解决问题的步骤，设计一条流水线，机械式的思维方式
优点：复杂的问题流程化，进而简单化
缺点：可扩展性差

面向对象：核心就是对象二字，对象就是特征与技能的结合体
优点：可扩展性强，
缺点：编程复杂度高
应用场景：用户需求经常变化，互联网应用，游戏，企业内部应用

类就是一系列对象相似的特征与技能的结合体
强调：站在不同的角度，得到的分类是不一样的
在现实世界中，一定先有对象，后有类
在程序中：一定得先定义类，后调用类
"""
# 先定义类
class LuffyStudent:
    school='luffycity'
    def learn(self):
        print('is learning')
    def eat(self):
        print('is eating')
    def sleep(self):
        print('is sleeping')
        return 1

# 后产生对象
stu1=LuffyStudent()
stu2=LuffyStudent()
stu3=LuffyStudent()
print(stu1.sleep())
