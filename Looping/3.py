i, j, flag = 0, 0, 0
n=int(input("Enter number: "))
n2=int(input("Enter number: "))
for i in range(n,n2+1):
    if (i == 1):
            continue
    flag = 1
          
    for j in range(2, i // 2 + 1):
        if (i % j == 0):
            flag = 0
            break
    if (flag == 1):
        print(i, end = " ")
    