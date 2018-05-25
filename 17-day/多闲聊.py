from socket import *
from threading import Thread

s = None
ip = ""
port = 0

def send():
	while True:
		content = input("请输入内容")
		s.sendto(content.encode("gb2312"),(ip,port))

def recv():
	while True:
		msg = s.recvfrom(1024)
		print("\r%s----%s\n请输入内容"%(msg[0].decode("gb2312"),msg[1][0]),end="")

def main():
	global s 
	global port
	global ip 
	ip = input("请输入对方ip:")
	port = int(input("请输入对方端口"))
	s = socket(AF_INET,SOCK_DGRAM)

	#绑定端口
	s.bind(("",6666))
	t = Thread(target = send)
	t1 = Thread(target= recv)
	

	t.start()
	t1.start()

	t.join()
	t1.join()

	s.close()

if __name__ == "__main__":
	main()
