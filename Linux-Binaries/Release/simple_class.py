class SimpleClass:
	def __init__(self, message):
		print "Constructor:  " , message
		
	def multiply(self, a, b):
		print "Will compute", a, "times", b
		c = 0
		for i in range(0, a):
			c = c + b
		return c
		
	def hello(self):
		print "Hello World!"