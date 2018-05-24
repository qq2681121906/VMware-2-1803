class Kebab:
    def __init__(self):
        self.cookedlever = 0
        self.cookedstr = "生的"
        self.condliments = []
    def cook(self,time):
        self.cookedlever += time
        if self.cookedlever>8:
            self.cookedstr = "烤成碳了"
