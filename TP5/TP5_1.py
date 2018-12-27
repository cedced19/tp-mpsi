#!/usr/bin/python3

a,b= 1,2
print(globals())
print(locals())

def f(x, y):
	print('A:', locals())
	a=3
	print('B:', locals())
	def g(z):
		print('C:',locals())
		a=4;b=5
		print('D:',locals())
		print('E:',globals())
	print('F:',locals())
	g(6)
	print('G:',locals())

f(10,20)
print(a, b)
print(globals())