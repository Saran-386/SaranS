n=int(input("Enter no of items: "))
list1=[]
for i in range(n):
	h=str(input("Enter item: "))
	list1.append(h)

listl=[]
for j in list1:
    k=len(j)
    listl.append(k)
print(listl)
print(max(listl))