e=0
o=0
lower=int(input("Enter lower range: "))
upper=int(input("Enter upper range: "))
for i in range(lower,upper+1):
    if (i%2==0):
        e=e+1
    else:
        o=o+1

print("Even, ",e)
print("Odd, ",o)