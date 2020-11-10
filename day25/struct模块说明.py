import struct
res=struct.pack('i',128099)
print(res,type(res),len(res))
res1=struct.unpack('i',res)
print(res1)
res=struct.pack('l',128099)
print(res,type(res),len(res))
res1=struct.unpack('l',res)
print(res1)