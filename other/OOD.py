# OOD practice in Python 

# implementation of shape classes in PIE p160

class Shape(object):
	''' abstract class for all shapes '''
	def __init__(self, center):
		self.center = center
	def get_center(self, center):
		return center
	def get_bounds(self):
		''' abstract method '''
		raise NotImplementedError("Abstract method of Shape!")
	def draw(self):
		''' abstract method '''
		raise NotImplementedError("Abstract method of Shape!")

class Rectangle(Shape):
	''' subclass of Shape '''
	temp = 1
	def __init__(self, center, w, h):
		super(Rectangle,self).__init__(center)
		self.w = w
		self.h = h
	def get_bounds(self):
		return self
	def get_width(self):
		return self.w
	def get_height(self):
		return self.h
	def draw(self):
		pass

	
class Ellipse(Shape):
	''' subclass of Shape '''
	def __init__(self, center, a, b):
		super(Ellipse,self).__init__(center)
		self.a = a
		self.b = b
	def get_bounds(self):
		return Rectangle(self.center, self.a*2, self.b*2)
	def get_semi_major_axis(self):
		return self.a
	def get_semi_minor_axis(self):
		return self.b
	def draw(self):
		pass
		
class Point(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
		
# rec = Rectangle(Point(1,2), 1, 2)
# print rec.get_width()
# print Rectangle.temp
# rec1 = type(rec)(Point(2,3),1,1)
# print type(rec1)
# print rec1.get_height()


# Multiple inheritance

# class First(object):
# 	def __init__(self):
# #		super(First, self).__init__()
# 		print("first")
# 
# class Second(object):
# 	def __init__(self):
# 		super(Second, self).__init__()
# 		print("second")

class Third(object):
# 	def __init__(self):
# 		super(Third, self).__init__()
# 		print("that's it")
	pass
 
print Third.__mro__
Third()

















		