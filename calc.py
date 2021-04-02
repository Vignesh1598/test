def add(x,y):
	return x+y

def subtract(x,y):
	return abs(x-y)

def multiply(x,y):
	return x*y

def divide(x,y):
	return x/y

while(True):
	p=input().split()
	op=p[0]
	if op == 'q':
		break
	x=float(p[1])
	y=float(p[2])

	if op=='add' or op=='a':
		print(add(x,y))

	if op=='subtract' or op=='s':
		print(subtract(x,y))

	if op=='multiply'  or op=='m':
		print(multiply(x,y))

	if op=='divide' or op=='d':
		print(divide(x,y))


