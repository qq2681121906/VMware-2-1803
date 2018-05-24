from socket import *

s = socket(AF_INET,SOCK_STREAM)

s.connect(("192.168.43.232",8888))

while True:
    sendData = input("请输入要发送的数据:")
    s.send(sendData.encode("gb2312"))

nsg = s.recv(1024)

print(msg.decode("gb2312"))

s.close()
