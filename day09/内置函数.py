"""
今日内容：
   1、二分法=>算法
   2、面向过程编程思想
   3、函数式
        lambda
        map
        filter
        reduce
        sorted
        max
        min
    4、模块
        import time
        time.sleep()
        time.strftime()
    5、内置函数
"""
#算法是高效解决问题的办法
#算法之二分法
#需求：有一个按照从小到大顺序排列的数字列表
#需要找到想要的那个数字，如何更高效？
# nums=[-3,4,7,10,13,21,43,77,89]
# find_num=90
# def binary_search(find_num,nums):
#     print(1)
#
#     if len(nums)==0:
#         return
#     mid_index=len(nums)//2
#     mid_value=nums[mid_index]
#     if find_num>mid_value:
#         nums=nums[mid_value+1:]
#         print(nums)
#         binary_search(find_num, nums)
#     elif find_num<mid_value:
#         nums = nums[:mid_value]
#         print(nums)
#         binary_search(find_num, nums)
#     elif find_num==mid_value:
#         print(mid_index)
#     else:
#         print('未查询到想要找的值')
#
# binary_search(find_num,nums)

#面向过程的编程思想：
#   核心是“过程”二次，过程即流程，指的是做事的步骤：先什么、再什么、后干什么
#   基于该思想编写程序就好比在设计一条流水线

#   优点：复杂的问题流程化、进而简单化
#   缺点：扩展性非常差

# 面向过程的编程思想应用场景解析：
# 1、不是所有的软件都需要频繁更迭：比如编写脚本
# 2、即便是一个软件需要频繁更迭，也并不代表这个软件所有的组成部分都需要一起更迭
# def zip(file):
#     pass
#
# def cloud_update(file):
#     return file
#
# def unzip(file):
#     return file
#
# file=zip('file')
# file1=cloud_update(file)
# unzip(file1)

#函数式编程：
lambda x,y:x+y
# 调用匿名函数
res=lambda x,y:x+y
print(res(1,2))
#真正的调用方法：临时调用一次的场景：更多的是将匿名与其他函数配合使用
salaries={
    'siry':3000,
    'tom':7000,
    'Lily':10000,
    'jack':2000
}
#找出薪资最高的那个人
#方法一
# def func(k):
#     return salaries[k]
# res=max(salaries,key=func)
# print(res)
# res1=max(salaries,key=lambda k:salaries[k])
# print(res1)
# #按姓名排序
# res2=sorted(salaries)
# print(res2)
# #按薪资排序
# res2=sorted(salaries,key=lambda k:salaries[k])
# print(res2)

#map的应用：全图
# l=['alex','lxx','wxx','xxq']
# new_l=(name+'_dsb' for name in l)
# print(new_l)
# new_l2=map(lambda name:name+'_dsb',l)
# print(new_l,new_l2)
# res=(name for name in l if name.endswith('sb'))
# print(res)
# #filter:筛选
# res1=filter(lambda name:name.endswith('sb'),l)
# print(res1)
# #reduce的应用
# from functools import reduce
# res=reduce(lambda x,y:x+y,[11,22,33],10)
# print(res)
#
# res1=filter(lambda name:name.endswith('q'),l)

"""
1、什么是模块：一系列功能的集合体
内置模块、第三方模块、自定义（python、已被编译的共享库或DLL的c、c++扩展库）
把一系列模块组织到一起的文件夹（文件夹下需要有__init.py__，该文件夹称之为包）
使用C编写并链接到python解释器的内置模块
把文件夹下
2、为何要用模块？
内置与第三的模块无需定义，可提升开发效率

"""
#导入文件做的三件事：
#1、执行模块py文件
#2、产生py文件的名称空间，将运行过程中产生的名字都丢到foo的名称空间
#3、在当前文件中产生的有一个名字foo，该名字指向2中产生的名称空间
#之后的导入，都是直接引用首次产生的foo.py

#2、引用：
#import foo
#foo.x
#强调1：模块名.名字，是指名道姓地问某一个模块
#强调2：无论是查看还是修改都是以原模块为基准，与调用无关

#3、可以以逗号为分隔符在一行导入多个模块，但是并不建议这么写

#4、导入模块的规范
# 1、内置
# 2、第三方
# 3、程序员自定义
# 5、可以通过as对模块重命名
# 6、模块是第一类对象
# 7、自定义的命名应该采用纯小写+下划线的风格






