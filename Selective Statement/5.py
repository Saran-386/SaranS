a =int(input("enter 1st side: "))
b =int(input("enter 2nd side: "))
c =int(input("enter 3rd side: "))
if(a**2==b**2 + c**2 or b**2==a**2 + c**2 or c**2==b**2 + a**2):
    print("1")
else:
    print("0")

