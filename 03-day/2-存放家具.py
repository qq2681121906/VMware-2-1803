class Home():
    def __init__(self,area):
        self.area = area
        self.containsItem = []
    def __str__(self):
        msg = "当前房间的面积为:"+ str(self.area)
        if len(self.containsItem) > 0:
            msg = msg + "容纳的物品有:"
            for temp in self.containsItem:
                msg = msg + temp.getName() + ", "
            msg = msg.strip(", ")
        return msg
    def accommodateItem(self,item):
        needArea = item.getUsedArea()
        if self.area > needArea:
            self.containsItem.append(item)
            self.area -= needArea
            print("已放到房间中")
        else:
            print("可用面积为%d,但放物品的面积为%d"%(self.area,needArea))
class Bed:
    def __init__(self,area,name = "床"):
        self.name = name
        self.area = area
    def __str__(self):
        msg = "床的面积为" + str(self.area) 
        return msg
    def getUsedArea(self):
        return self.area
    def getName(self):
        return self.name
newHome = Home(100)
print(newHome)
newBed = Bed(20)
print(newBed)
newHome.accommodateItem(newBed)
print(newHome)
newBed2 = Bed(30,"席梦思")
print(newBed2)
newHome.accommodateItem(newBed2)
print(newHome)

