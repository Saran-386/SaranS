s=str(input("Enter string: "))
l=len(s)
if (l%5==0):
    a=s[::-1]
    print(a.upper())
else:
    print("Given string length is not a multiple of 5")