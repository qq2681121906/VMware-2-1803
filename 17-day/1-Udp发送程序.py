from socket import *

s = socket(AF_INET,SOCK_DGRAM)

s.sendto("哈哈".encode("gb2312"),("192.168.43.232",8888))

#content,info = s.recvfrom(1024)

#print("%s-----%s"%(content.decode("gb2312"),info[0]))
s.close()
