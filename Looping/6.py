n=int(input("Enter number: "))
n2=int(input("Enter number: "))
for j in range(n,n2+1):
    for i in range(1,j+1):
        print(j," x ",i,'=',j*i)
    print("\n")
