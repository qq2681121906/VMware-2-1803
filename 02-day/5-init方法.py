class Boy:
    def __init__(self,age,height):
        self.age = age
        self.height = height
        self.address = "东北"
        self.games = []
        for i in range(5):
            list = input("请输入游戏")
            self.games.append(list)
    def study(self):
        print("学习")

    def opencar(self,car):
        print("一定会开车%s"%car)

    def showage(self):
        print("年龄%d"%self.age)

    def showgames(self):
        for i in self.games:
            print(i)

nasiyuan = Boy(19,170)
nasiyuan.study()
nasiyuan.opencar("路虎")
nasiyuan.showage()
nasiyuan.showgames()
