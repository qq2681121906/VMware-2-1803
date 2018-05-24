from multiprocessing import Process
import time

class Dog(Process):

    def __init__(self):
        Process.__init__(self)

    def run(self):
        for i in range(5):
        time.sleep(1)
        print("Process dog")
