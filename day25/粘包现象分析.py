#粘包现象：一次只取1024个字节，会造成数据一次取不完，下次才能取
#UDP协议不会出现粘包现象
#1、不管是recv还是send都不是直接接收对方的数据，而是操作自己的操作系统内存--->不是一个send对应一个recv
#2、recv：
wait data 耗时非常长
copy data
send:
copy data