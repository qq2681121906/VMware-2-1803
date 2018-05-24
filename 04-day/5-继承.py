class Animal(object):
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("吃")
    def move(self):
        print("移动")
class Cat(Animal):
    pass
class Dog(Animal):
    pass
tom = Cat("tom")
tom.eat()
tom.move()
print(tom.name)

