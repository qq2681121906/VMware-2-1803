class Pig():

    def sleep(self):
        a = input("请输入内容")
        print(a)
   
    def eat(self):
        print("猪饲料")

    def introduce(self):
        print("我叫%s年龄%d颜色%s"%(self.name,self.age,self.color))

peiqi = Pig()#创建对象
peiqi.age = 12
peiqi.color = "粉色"
#peiqi.name = "小猪佩奇"
peiqi.name = input("请输入名字")
peiqi.eat()#调用对象的方法
peiqi.sleep()#调用对象的方法
peiqi.introduce()#调用自我介绍

qz = Pig()
qz.age = 10
qz.color = "蓝色"
qz.name = "乔治"
qz.eat()
qz.sleep()
qz.introduce()
