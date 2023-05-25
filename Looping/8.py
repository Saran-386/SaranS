n=int(input("Enter lower range: "))
n2=int(input("Enter upper range: "))
for i in range(n,n2+1):
    order = len(str(i))
    s = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        s += digit ** order
        temp //= 10
    print(s)
    break