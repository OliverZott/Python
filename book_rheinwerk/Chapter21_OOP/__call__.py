"""
Magic Methods: __call__  __init__  __del__

init:
- 	Constructor: builds instance of class

call:
-	In python instances of classes (objects) can be used as if they were functions (first class objects). To do that a __call__ class function has to be defined
-	Allows instance to be used as function
-	Defines function body which is executed when instance is used as function

source: StackOverflow - 9663562
Author: Oliver Zott
Date: 18.09.2019
"""


class Stuff(object):

	def __init__(self, x, y, range):
		super(Stuff, self).__init__()
		self.x = x
		self.y = y 
		self.range = range
		
	def __call__(self, x, y):
		self.x = x
		self.y = y
		print("__call__ with (%d, %d)" %(self.x, self.y))


"""	
	def __del__
		del self.x
		del self.y 
		del self.range
"""


def main():
	s = Stuff(4, 6, 12)
	print("print(s.x): {}".format(s.x))
	print("print(s.y): {}".format(s.y))
	print("print(s): {}".format(s))

	print()
	# print("print(s(1,2)): {}".format(s(1, 2)))
	# print("print(s(1,2)): %d" % (s(1, 2)))
	s(1, 2)


if __name__ == '__main__':
	main()