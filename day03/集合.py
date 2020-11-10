# 1、集合
# friends1 = ['li', 'zha', 'lei']
# friends2 = ['zuo', 'zha', 'lei']
# 2、定义：在{}内用逗号分隔开，不可重复
# s = {} #默认是空字典
# 定义空集合
# s = set()
# print(s, type(s))
# 3、类型转换，set会去重
# set({1,2,3})
# set(1,2,[1,2])# 会报错，列表是可变的
# 4、内置方法：
friends1 = {'li', 'zha', 'lei'}
friends2 = {'zuo', 'zha', 'lei'}
# 4.1 取交集
# res = friends1 & friends2
# print(res)
#4.2 取并集
# res = friends1|friends2
# print(res)
#4.3 取差集，friends1独有的，注意顺序
# res = friends1-friends2
# print(res)
#4.4 对称差集：取两个用户的独有好友
# res = friends1-friends2|friends2-friends1
# res1 = friends1^friends2
# print(res,res1)
#4.5 父子集：包含关系
# s1={1,2,3}
# # # s2={1,2}
# # # print(s1>s2)
# 去重
# 1、只能针对不可变类型去重
print(set([1,1,1,1,2]))
# 2、无法保证原来的顺序

# for循环
#其他内置方法
s={1,2,3,4}
s1={1,2,3,4}
s.discard(1)#删除对象
s.update(5,4)#加入后并去重
s.pop()#随机删除
s.isdisjoint(s,s1)# 两个集合完全独立，返回True