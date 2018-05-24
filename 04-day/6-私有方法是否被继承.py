class Father():
    def __init__(self):
        self.__girl_count = 4
    def getGirlCount(self):
        return self.__girl_count
    def makemoney(self):
        print("我会挣钱")
    def eat(self):
        print("会吃饭")
    def __girl(self):
        print("处对象方法大全")
    def askGirl(self):
        self.__girl()
class Son(Father):
    pass
xiaoming = Son()
xiaoming.makemoney()
xiaoming.eat()
xiaoming.askGirl()
print(xiaoming.getGirlCount())
