class hulu():
    def gongneng(self):
        print("打妖怪")
    def zuoyong(self):
        print("保护老头")
    def xunzhao(self):
        print("找个奶奶")
    def ziwojieshao(self):
        print("我是%s年龄%d颜色%s"%(self.name,self.age,self.color))
dawa = hulu()
dawa.age = 7
dawa.color = "红色"
dawa.name = "老大"
dawa.gongneng()
dawa.zuoyong()
dawa.xunzhao()
dawa.ziwojieshao()

