s = str(input("Enter the string: "))
if (len(s)<=2):
    print("Empty string")
else:
    print(s[0:2])
    l=len(s)
    print("\n",s[l-2:l])