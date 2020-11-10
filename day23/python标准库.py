#1、什么是序列化
# 序列化指的是把内存的数据类型转换成一个特定的格式的内容
# 该格式的内容可用于存储或者传输给其他平台使用
# 内存中的数据类型--->序列化--->特定的格式（json格式或者pickle格式）
# 内存中的数据类型<---反序列化<---特定的格式（json格式或者pickle格式）


#2、为何要序列化
# 序列化得到的结果=>特定的格式的内容有两种用途
# 1、可用于存储=》用于存档
# 2、传输给其他平台使用=》跨平台数据交互
# 强调：
#       针对用途1的特定一格式：可以是一种专用的格式=》pickle只有python可以识别
#       针对用途2的特定一格式：应该是一种通用，能够被所有语言识别的格式=》json

#3、如何序列化与反序列化
import json
# 序列化
# res=json.dumps([1,'aaa',True,False])
# print(res)
# with open('test.json',mode='wt',encoding='utf-8') as f:
#     f.write(res)
# # 将序列化结果写入文件的简单方法
# with open('test.json',mode='wt',encoding='utf-8') as f:
#     json.dump([1,'aaa',True,False],f)
#
# # 反序列化
# with open('test.json',mode='rt',encoding='utf-8') as f:
#     res1=f.read()
#     l=json.loads(res1)
#     print(l)
# # 反序列化读json格式的简单方法
# with open('test.json',mode='rt',encoding='utf-8') as f:
#     l=json.load(f)
#     print(l)

# json验证:json格式兼容的是所有语言通用的数据类型
# json.dumps({1,2,3,4,5})
# 强调：json格式没有单引号，没有大写字母
l=json.loads('[1,"aaa",true,false]')
print(l[0])

# 猴子补丁:应用于代码已经写成，再修改
# import json
# import ujson
# def monkey_patch_json():
#     json.__name__='ujson'
#     json.dumps=ujson.dumps
#     json.loads=ujson.loads
#
# monkey_patch_json()
# json()
# json()
# json()
# json()

# 了解知识
# import time
# print(time.asctime())
#
# import configparser
# config=configparser.ConfigParser()
# config.read('test.ini')
#
# # 获取某一section下的所有options
# print(config.options('section1'))
#
# #获取items
# print(config.items('section1'))
#
# # 获取items的参数值
# res=config.get('section1','k1')
# print(res,type(res))
# res=config.getint('section1','k1')
# res1=config.getboolean('section1','k1')
# res2=config.getfloat('section1','k1')

# 1、什么是hash
# 哈希是一类算法，该算法接受传入的内容，经过运算得到一串hash值

# hash的特点：
# 1、只要传入值守一样的，得到的hash值也是一定的
# 2、不能根据hash值反推出来传入的内容
# 3、只要使用的hash算法不变，无论校验的内容有多大，得到的hash值长度不变


# 用途
# 1、敏感信息加密
# 2、文件完整性校验
# import hashlib
# m=hashlib.md5()
# m.update('hello'.encode('utf-8'))
# m.update('world'.encode('utf-8'))
# res=m.hexdigest()
# print(res)
# print(m)
# # 文件加密的思路：随机取多个文件位置的地方，n个字节去进行加密
# f=open('a.txt',mode='rb')
# f.seek()
#
# # 撞库
# cry=2222
# passwd={
#     '111',
#     '222'
# }
# dic={}
# for p in passwd:
#     res=hashlib.md5(p.encode('utf-8'))
#     dic[p]=res.hexdigest()
#
# for k,v in dic.items():
#     if v == cry:
#         print('撞库成功')
#
# # 密码加盐
# m=hashlib.md5()
# m.update('盐值'.encode('utf-8'))
# m.update('密码'.encode())

import subprocess
obj=subprocess.Popen('ls /root;dir;echo 1',shell=True,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE)
print(obj)
res=obj.stdout.read()
print(res)
err_res=obj.stderr.read()
print(err_res.decode('gbk'))

