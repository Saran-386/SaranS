ch=1
list1=[]
while(ch!=0):
    ch=int(input("Enter choice: "))
    h=int(input("Enter item: "))
    list1.append(h)

list1.sort()
print(list1)