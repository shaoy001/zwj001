# 元祖就是"一个不可变的列表" type
# 1、作用：按照索引/位置存放多个值，只用于读不用于改
# 2、
t = (10) # 单独一个括号代表包含的意思
print(type(t))

t = (10,)  #如果元祖只有一个元素，必须加逗号
print(type(t))
# 元祖里面的元素如果是列表，则列表内的值可更改，列表不可更改
# 3、类型转换：但凡能够被for循环遍历的类型都可以当作参数传给list()转换成列表
res = tuple({'k1': 111, 'k2': 222, 'k3':333})
print(res)
aa = tuple('hello')
print(aa[1])
# 内置方法
# 4.1 优先掌握：按索引取值
msg = (111, 'egon', 'hello')
# 正向取
# 反向取
# 可以取也可以改，索引不存在时，则报错
# print(msg[5])
# 字符串只能取
# 4.1.2 切片|步长|反向步长
# res = msg[0:5:2]
# res = msg[5:0:-1]
# res = msg[::-1]  # 把字符串倒过来
# res = msg[:5]
print(msg[0:len(msg)])
msg1 = msg[:]
print(msg1)  # 切片相当于拷贝行为，而且相当于浅拷贝
# print(res, '\n', msg)
# 4.1.3 len
# print(len(msg))
# 4.1.4 in |not in



