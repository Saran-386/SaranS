n=int(input("Enter no of items: "))
list1=[]
for i in range(n):
	h=int(input("Enter item: "))
	list1.append(h)
	
e, o = 0, 0
for num in list1:
	if num % 2 == 0:
		e += 1
	else:
		o += 1
print("Even numbers in the list: ", e)
print("Odd numbers in the list: ", o)
