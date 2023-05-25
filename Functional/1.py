import math
def ps(x):
    if(x >= 0):
        sr = int(math.sqrt(x))
        return ((sr*sr) == x)
    return False

x= int(input("Enter number: "))
if (ps(x)):
    print("Yes")
else:
    print("No")