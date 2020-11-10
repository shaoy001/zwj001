import socket
import struct
import json

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('106.12.12.209',8080))

while True:
    msg = input('please inmput cmd>>>: ').strip()
    if not msg: continue
    phone.send(msg.encode('utf-8'))
    #第一步：先拿收报头的长度
    obj=phone.recv(4)
    header_size=struct.unpack('i',obj)[0]
    #第二步：再收报头
    head_bytes=phone.recv(header_size)
    #第三步：从报头中解析出真实数据的描述信息
    header_json=head_bytes.decode('utf-8')
    header_dic=json.loads(header_json)
    total_size=header_dic['total_size']
    #第二步：接收真实的数据
    recv_size=0
    recv_data=b''
    while recv_size<total_size:
        res = phone.recv(1024)
        recv_data += res
        #print(recv_data)
        recv_size +=len(res)
    print(recv_data)
phone.close()
