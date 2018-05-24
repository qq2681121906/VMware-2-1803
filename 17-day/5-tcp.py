from socket import *

#创建一个tcp的套接字
s = socket(AF_INET,SOCK_STREAM)

#绑定端口

s.bind(("",8888))

#监听最大的连接数

s.listen(5)

#等着新的客户端接入
newSocket,info = s.accept()

#取消息
while True:
    content = newSocket.recv(1024)
    print(content.decode("gb2312"))
