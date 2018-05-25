from socket import *

s = socket(AF_INET,SOCK_STREAM)

s.connect(("192.168.204.129",8888))

while True:
    sendData = input("请输入要发送的数据:")
    s.send(sendData.encode("gb2312"))

nsg = s.recv(1024)

print(nsg.decode("gb2312"))

s.close()
