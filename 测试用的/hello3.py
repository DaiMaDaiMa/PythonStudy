def config(a,b):
	def line(x):
		return a*x+b
	return line
	


line = config(1,2)
print(line(5))
