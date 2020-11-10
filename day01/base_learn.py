#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Author : Ayden Lee
    Date   : 06/27/2020
    Desc   :
    Change LOG :

"""
# for i in range(1, 9, 2):
#     if i == 5:
#         continue
#     for j in range(5):
#         print(i, j)

# print('hello', end='*')
# print('world')
#
# age = 10
# print(id(age), type(age))

# x = int(10)
# name = input('xxx')

# 类型转换
# 2.1 纯数字的字符串转成int
# 2.2 (了解)

# salary = int("3.1")
# print(salary)

# msg = "hello"
# print(type(msg))

# 4、使用：内置方法
# 4.1 优先掌握：按索引取值
# msg = 'hello,world!'
# print(msg[5])
# 字符串只能取
# 4.1.2 切片|步长|反向步长
# res = msg[0:5:2]
# res = msg[5:0:-1]
# res = msg[::-1]  # 把字符串倒过来
# res = msg[:5]
# print(res, '\n', msg)
# 4.1.3 len
# print(len(msg))
# 4.1.4 in |not in
# 4.1.5 移除字符串左右两侧的空白strip，但是不会更改原字符串
# msg = '!@#$%%^^&&&sss***'
# print(msg.strip('%*!@#$'))
# strip('去除的字符')
# 4.1.6 切分split，默认分隔符是空格;切分次数('',n)
# msg = 'mongos#config#shard'
# info = msg.split("#", 1)
# print(info)
# 4.1.7 循环
# for i in msg:
#    print(i)

# 4.2 需要掌握
# lstrip、rstrip
# lower、upper
# startswith,endswith
# rsplit:从右往左切
# join:按照某个分隔符，把列表拼接成字符串
# l = [1, 'b', 'c']
# m = ".".join(l)
# print(m)
# replace：替换(old,new,once)
# isdigit：判断字符串是否由纯数字组成
# if age.isdigit()

# 4.3 了解
# 4.3.1 find,index index找不到会抛出异常，find则返回-1
# center，居中补足;ljust：字符串居左；rjust：字符串居右
print('egon'.center(50, '*'))
# expandtabs:制表符；swapcase：大小写转换；title：单词首字母大写
# islower,isupper,istitle,isalnum(字母或数字)，isalpha(由字母组成)，isspace（字符串由空格组成）
# isidentifier(是否作为自定义变量合法)