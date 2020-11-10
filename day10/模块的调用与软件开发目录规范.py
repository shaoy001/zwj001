
# import foo
# from foo import get
# x=2
# foo.get()
# foo.change()
# foo.change()
# print(x)
# get()
# 循环导包可能引发问题，可通过在函数内导包解决
#import sys
# 值为一个列表，存放了一系列的文件夹
#其中第一个文件夹是当前执行文件所在的文件夹
#print(sys.path)
# 导入优先级
# 1、从内存拿
# 2、从硬盘
# 了解：sys.modules查看已经加载到内存中的模块
# 导入包后，del或其他操作无法直接删除内存地址，
# import sys
# sys.path.append(r'../day09')
# import foo1
# # python是一门解释性强类型的动态性语言
# # 可按如下提示，但是不会报错
# def register(name:str,age:int,hobbies:tuple)->int:
#     print(name)
#     print(age)
#     print(hobbies)
#     return 111
# register(1,'aaa',99)
# print(register.__annotations__)
"""
1、包就是一个包含有__init__.py文件的文件夹

2、为何要有包
    包的本质上模块的模块的一种形式，包上用来被当作模块导入
"""
#文件夹可以直接做成一个包
# import mm
# mm.hhh()
#包的使用
#凡是在导入时候，“.”的左侧必须是一个包
#可以带一连串的点，但都必须遵守规则
#相对导入：仅限于包内使用，不能跨出包（包内模块之间的导入，推荐相对导入）
#.：当前文件夹
#..:上一层文件夹
"""
1、
"""




