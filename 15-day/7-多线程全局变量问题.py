from threading import Thread
import time

g_num = 100

def work1():
    global g_num
    for i in range(1000000):
        g_num += 1

    print("----in work1, g_num is %d---"%g_num)


def work2():
    global g_num
    for i in range(1000000):
        g_num+=1
    print("----in work2, g_num is %d---"%g_num)


print("---线程创建之前g_num is %d---"%g_num)

t1 = Thread(target=work1)
t1.start()

t2 = Thread(target=work2)
t2.start()
