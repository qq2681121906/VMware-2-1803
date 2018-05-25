def w(cls):
	def w1(*args,**kwargs):
		return cls(2)
	return w1

#@w 相当于 Dog = w(Dog)
@w
class Dog(object):
	def __init__(self,x = 0):
		self.x = x

dog = Dog(1)
print(dog.x)

dog = Dog(3)
print(dog.x)

### Dog(2)
