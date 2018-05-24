class ShowError(Exception):
    def __init__(self,len,leastlen):
        self.len = len
        self.leastlen = leastlen




def main():
    try:
        s = input("请输入")
        if len(s)<3:
            raise ShowError(len(s),3)
    except ShowError as ret:
        print("你传的值是%d,至少是%d位"%(ret.len,ret.leastlen))
main()
