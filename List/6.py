n=int(input("Enter no of items: "))
list1=[]
for i in range(n):
	h=int(input("Enter item: "))
	list1.append(h)

i,j,flag=0,0,0
for i in list1:
    if (i == 1):
            continue
    flag = 1
          
    for j in range(2, i // 2 + 1):
        if (i % j == 0):
            flag = 0
            break
    if (flag == 1):
        print(i, end = " ")
        print("True")