list1=[]
for i in range(5):
	h=int(input("Enter item: "))
	list1.append(h)
flist=[]
f=1
for num in list1:
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
         print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
              f = f*i
        flist.append(f)

print(list1)
print(flist)