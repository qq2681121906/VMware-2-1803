from thereading import Thread
import time
import threading

def work():
    name = threading.current_thread().name
    print(name)
    num = 1
    if name == "Theead-1":
        num += 1
        time.sleep(1)
        print("呵呵呵%d"%num)
    else:
        time.sleep(1)
        print("哈哈哈%d"%num)

"""
def work1():
    name = threading.current_thread().name
    print(name)
    time.sleep(2)
    num = 100
"""
