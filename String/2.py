def swap(a):
    a=s.split(" ")
    t=str()
    t=a[0][0:2]
    a[0][0:2]=a[1][0:2]
    a[1][0:2]=t
    print(a)
s = str(input("Enter the string: "))
swap(s)