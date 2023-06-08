def series(n,x):
	d=2
	s=0
	for i in range(0,n+1):
		s = s + (x/d)
		d=d*2
	print(s)

num = int(input("N = "))
x = int(input("X = "))
series(num,x)
