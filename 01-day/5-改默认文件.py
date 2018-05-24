import os
name = input("亲输入文件名")
j = os.listdir(name)
for i in j:
    po = i.rfind(".")
    x_name = i[0:po]+"那思源"+i[po:]
    os.chdir("/home/nasiyuan/桌面/2-1803/01-day/游戏")
    os.rename(i,x_name)
