#
# 定义：{}内用逗号分隔开多个key:value，其中value可以使用任意类型，但是key必须是不可变类型

#数据转换类型
#dict()
#快速造字典：
# keys = ['name', 'age', 'gender']
# d = {}.fromkeys(keys, None)
# 针对赋值操作，key存在，则修改，key不存在，则创建新值
# 删除
# del d['key']
# d.pop，根据key删除元素，返回删除的key的对应值
# d.popitem(),随机删除，返回元祖
# d.update({'k2':222}) 有则更新，无则加上
# d.get('k2') # key不存在不报错，返回None，d['k2']不存在会报错
# d.setdafault('') 如果key有则不添加，如果key没有则添加，返回字典中key对应的值
d = {}
d.setdefault('aa', 'bb')
d.setdefault('aa', )
print(d)
