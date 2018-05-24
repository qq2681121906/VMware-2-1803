class Car():

    def __init__(self):
        drlf.color = "黄色"

    def move(self):
        print("车开始跑")
    
    def stop(self):
        print("车停了")

bmw = Car()
print("颜色是%s"%bmw.color)
bmw.move()
bmw.stop()
