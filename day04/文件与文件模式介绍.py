# coding:utf-8
#  1、如何用文件：open()
# 控制文件读写内容的模式：t和b
# 强调：t和b不能单独使用，必须跟r/w/a连用
# t文本(默认的模式)
# 1、读写都以str(unicode)为单位的
# 2、文本文件
# 3、必须指定encoding='utf-8'
# b二进制/byte
# 控制文件读写操作的模式
# r 只读模式
# w 只写模式
# a 只追加写模式
# +：r+、w+、a+
# 1、打开文件
# open('C:/a/b/c')
# open(r'C:\a\b\c')  # 推荐
# 2、文件类型
# f的值是一种变量
# f = open('file1',encoding='UTF-8')
# print(f)
# res = f.read()
# print(res)
# f.close() #回收操作系统资源
# with上下文文件管理：文件对象又称为文件句柄，可以加“，”打开多个文件
# with open('file1', mode='rt', encoding='UTF-8') as f:
#     res=f.read()
#     print(res)
# r模式(默认的操作模式):只读模式,不存在则报错
# with open('file1',mode='rt',encoding='utf-8') as f:
#     print('第一次读'.center(50,'*'))
#     res = f.read()  # 把内容从硬盘读入内存
#     print(res)
# # with open('file1',mode='rt',encoding='utf-8') as f:
#     print('第二次读'.center(50,'*'))
#     res1 = f.read()  # 把内容从硬盘读入内存
#     print(res1)
# inp_username = input('your name>>:').strip()
# inp_password = input('your password>>:').strip()
# # 验证
# with open('user.txt',mode='rt',encoding='utf-8') as f:
#     for line in f:
#         username,password = line.strip().split(':')
#         if inp_username==username and inp_password==password:
#             print('login successfull')
#             break
#     else:
#         print('账号或密码错误')
# 2、w：只写模式，当文件不存在时会创建空文件，当文件存在时会清空
# with open('d.txt',mode='wt',encoding='utf-8') as f:
#     f.write('嘿嘿嘿\n')
#     f.write('哈哈哈')
# 3、a：只追加写，在文件不存在时会创建空文档，文件存在时，文件指针会跳转到末尾
# with open('d.txt',mode='at', encoding='utf-8') as f:
# #    f.read()  # 报错
#     f.write('哦哦哦')
# 4、x模式：只写模式，不可读；文件存在则报错，文件不存在则创建
# 5、b模式：控制内容
"""
t：默认模式
    1、读写都是以字符串（unicode）为单位
    2、只能针对文本文件
    3、必须指定字符编码，即必须指定
b：binary模式，二进制
    1、读写都是以bytes为单位
    2、可以针对所有文件
    3、一定不能指定字符串，即必须不能指定

总结：
1、在操作纯文本文件方面t模式帮我们省去了编码与解码的环节，b模式则需要手动解码
2、针对非文本文件（如图片、视频、音频等）只能使用b模式

"""
# with open('d.txt', mode='rt', encoding='utf-8') as f:
#     res = f.read()
#     print(res)
#
# with open(r'd.txt', mode='rb') as f:
#     res = f.read()
#     print(res, type(res))
#     print(res.decode())
# with open(r'd.txt', mode='wb') as f:
#     res = f.write('ss'.encode('utf-8'))
    # print(res, type(res))
    # print(res.decode())

# 循环读取文件
# 方式一：适合单行大文件
# with open(r'd.txt', mode='rb') as f:
#     while True:
#         res = f.read(1024)
#         if len(res) == 0:
#             break
#         print(len(res))
#方式二：
# with open(r'd.txt', mode='rt',encoding='utf-8') as f:
#     for line in f:
#         print(line)
#
# with open(r'd.txt', mode='rb') as f:
#     for line in f:
#         print(line)
# 操作文件的其他方法
# with open(r'd.txt', mode='rt',encoding='utf-8') as f:
#     res = f.readline()
#     res1 = f.readline()
#     print(res,res1)
#
# with open(r'd.txt', mode='rt',encoding='utf-8') as f:
#     res = f.readlines()
#     print(res)
# 写相关操作:f.writelines()
# with open(r'd.txt', mode='wt',encoding='utf-8') as f:
#     f.write('111\n222\n333\n')
#     l = ['111\n', '222', '333', 444]
#     f.writelines(l)
# 补充一
# with open(r'd.txt', mode='wb') as f:

    # l = [
    #     b'111\n',
    #     b'222',
    #     b'333'
    # ]
    # f.writelines(l)
# 补充2：'上'.encode('utf-8')等同于bytes('上',encoding='utf-8')
#     l = [
#         bytes('111\n', encoding='utf-8'),
#         bytes('222', encoding='utf-8'),
#         bytes('333', encoding='utf-8'),
#     ]
#     f.writelines(l)
#
# with open(r'd.txt', mode='wt',encoding='utf-8') as f:
#     f.write('哈哈')
#     f.flush()

# 控制文件指针操作，指针移动的单位都是以bytes/字节为单位
# 只有一种情况特殊：
#       t模式下的read(n),n代表的是字符个数
# with open('aa.txt', mode='rt', encoding='utf-8') as f:
#     res = f.read(4)
#     print(res)
# f.seek(n,模式):n指的是移动的字节个数
# 模式：
# 0：参照物是文件开头位置
# 1: 参照物是当前指针所在位置
# 2: 参照物是文件末尾位置，应该倒着移动
# f.seek(9, 0)
# f.seek(9, 1)
# f.seek(-9, 2)
# f.tell # 获取文件指针当前位置
# 强调：只有0模式可以在t下使用
def func():
    print(x)
    x = 3
x = 3
func()



