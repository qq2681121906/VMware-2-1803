class Father(object):
    def __init__(self,name,Colorofskin="黄种人"):
        self.name = name
        self.colorofskin = Colorofskin
    def run(self):
        print("%s在跑"%self.name)
class Theboy(Father):
    def setNewName(self,newName):
        self.name = newName
    def eat(self):
        print("%s在吃"%self.name)
nh = Theboy("闫子雄")
print("男孩的名字为:%s"%nh.name)
print("男孩的肤色为:%s"%nh.colorofskin)
nh.eat()
nh.setNewName("男孩")
nh.run()
