"""
先从服务器端说起。服务器端先初始化Socket，然后与端口绑定(bind)，
对端口进行监听(listen)，调用accept阻塞，等待客户端连接。
在这时如果有个客户端初始化一个Socket，然后连接服务器(connect)，
如果连接成功，这时客户端与服务器端的连接就建立了。客户端发送数据
请求，服务器端接收请求并处理请求，然后把回应数据发送给客户端，客
户端读取数据，最后关闭连接，一次交互结束
socket()模块函数用法
import socket
socket.socket(socket_family,socket_type,protocal=0)
socket_family 可以是 AF_UNIX 或 AF_INET。socket_type 可以是 SOCK_STREAM 或 SOCK_DGRAM。protocol 一般不填,默认值为 0。

获取tcp/ip套接字
tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

获取udp/ip套接字
udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

由于 socket 模块中有太多的属性。我们在这里破例使用了'from module import *'语句。使用 'from socket import *',我们就把 socket 模块里的所有属性都带到我们的命名空间里了,这样能 大幅减短我们的代码。
例如tcpSock = socket(AF_INET, SOCK_STREAM)
"""

import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(phone)
phone.bind(('127.0.0.1',8080))
phone.listen(5)
conn,client_addr=phone.accept()
#收发消息
while True:
    try:
        data=conn.recv(1024)#单位：bytes，1024代表最大接收1024个bytes
        if not data:break#适用于linux系统
        print('客户端的数据',data)
        conn.send(data.upper())
    except Exception as e:#适用于windows系统
        print(e)
        break
conn.close()
phone.close()
"""
服务端套接字函数
s.bind()    绑定(主机,端口号)到套接字
s.listen()  开始TCP监听
s.accept()  被动接受TCP客户的连接,(阻塞式)等待连接的到来

客户端套接字函数
s.connect()     主动初始化TCP服务器连接
s.connect_ex()  connect()函数的扩展版本,出错时返回出错码,而不是抛出异常

公共用途的套接字函数
s.recv()            接收TCP数据
s.send()            发送TCP数据(send在待发送数据量大于己端缓存区剩余空间时,数据丢失,不会发完)
s.sendall()         发送完整的TCP数据(本质就是循环调用send,sendall在待发送数据量大于己端缓存区剩余空间时,数据不丢失,循环调用send直到发完)
s.recvfrom()        接收UDP数据
s.sendto()          发送UDP数据
s.getpeername()     连接到当前套接字的远端的地址
s.getsockname()     当前套接字的地址
s.getsockopt()      返回指定套接字的参数
s.setsockopt()      设置指定套接字的参数
s.close()           关闭套接字
面向锁的套接字方法
s.setblocking()     设置套接字的阻塞与非阻塞模式
s.settimeout()      设置阻塞套接字操作的超时时间
s.gettimeout()      得到阻塞套接字操作的超时时间
面向文件的套接字的函数
s.fileno()          套接字的文件描述符
s.makefile()        创建一个与该套接字相关的文件
"""
#如果监听失败，报地址已经被使用：
#这个是由于你的服务端仍然存在四次挥手的time_wait状态在占用地址（如果不懂，请深入研究
#1.tcp三次握手，四次挥手
#2.syn洪水攻击
#3.服务器高并发情况下会有大量的time_wait状态的优化方法）
#加入一条socket配置，重用ip和端口
#方法一
# phone=socket(AF_INET,SOCK_STREAM)
# phone.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #就是它，在bind前加
# phone.bind(('127.0.0.1',8080))
#方法二
"""
发现系统存在大量TIME_WAIT状态的连接，通过调整linux内核参数解决，
vi / etc / sysctl.conf

编辑文件，加入以下内容：
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_fin_timeout = 30

然后执行 / sbin / sysctl - p
让参数生效。

net.ipv4.tcp_syncookies = 1
表示开启SYN
Cookies。当出现SYN等待队列溢出时，启用cookies来处理，可防范少量SYN攻击，默认为0，表示关闭；

net.ipv4.tcp_tw_reuse = 1
表示开启重用。允许将TIME - WAIT
sockets重新用于新的TCP连接，默认为0，表示关闭；

net.ipv4.tcp_tw_recycle = 1
表示开启TCP连接中TIME - WAIT
sockets的快速回收，默认为0，表示关闭。

net.ipv4.tcp_fin_timeout
修改系統默认的TIMEOUT时间
"""
