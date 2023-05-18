n=int(input("Enter lower range: "))
n2=int(input("Enter upper range: "))
for i in range(n,n2+1):
    order = len(str(i))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    print(i)