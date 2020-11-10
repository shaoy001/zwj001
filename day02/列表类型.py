# 3、类型转换：但凡能够被for循环遍历的类型都可以当作参数传给list()转换成列表
res = list({'k1': 111, 'k2': 222, 'k3':333})
print(res)
aa = 'hello'
print(aa[1])
# 内置方法
# 4.1 优先掌握：按索引取值
msg = [111, 'egon', 'hello']
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
# 4.1.5 追加 append
# msg.append(333)
# print(msg)
# # 4.1.6 插入值
# msg.insert(1, 'alex')
# print(msg)
# 4.1.7 列表拼接,extend可添加列表或字符串
# new_msg = ['ss']
# for i in new_msg:
#     msg.append(i)
# print(msg)
# msg.extend(new_msg)
# print(msg)
# 亚伦阿瑟36题
# 4.1.8 删除值
# 方式一：del通用的删除方法，只是单纯的删除，没有返回值
# del msg[0]
# 方式二：msg.pop,根据索引删，不指定索引，默认删最后一个
# pop会返回删除的对象
# mm = msg.pop()
# print(msg, mm)
# 方式三：msg.remove()根据元素删除
# msg.remove('hello')
# print(mm)
# 4.1.9 for循环
# 4.2 需要掌握
# msg.count()
# msg.index("对象")  # 找不到报错
# msg.clear()  # 清空
# msg.reverse()  # 将列表反转
# msg.sort()  # 排序,默认升序；列表内必须是同种类型
# 4.3 了解
# 4.3.1字符串可以比大小
# print('z' > 'abcde')
# 4.3.2 列表也可以比较大小，但是对应位置必须是同种类型
# print('z' > 'abcde')

# 补充
# 队列：FIFO first in first out
# msg.append('first')
# msg.append('second')
# msg.append('third')
# msg.pop(0)
# msg.pop(0)
# msg.pop(0)
# 堆栈：LIFO 后进先出

# msg.append('first')
# msg.append('second')
# msg.append('third')#
# msg.pop()
# # msg.pop()
# # msg.pop()


