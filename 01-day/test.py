
class Car(object):
	def _init_(self,newwheeLNum,newColor):
		self.wheelNum = newwheeLNum
		self.color = newColor

	def _str_(self):
		msg = "您好,车辆已经制造完毕,车辆的颜色是:"+self.color+",一共:"+str(self.wheelNum)+"个轮子"
		return msg

	def move(self):
		print("车再跑,目标:台湾")

# 创建对象
msld = Car(6,"green")
# 判断玛莎拉蒂是不是车类
isCar = isinstance(msld,Car)
print("*"*20,isCar,"*"*20)
print("车轮的颜色为:%s"%msld.color)
print("车轮胎的数量:%s"%msld.wheelNum)
