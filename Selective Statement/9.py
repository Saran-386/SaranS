print("Rating will be ( 1 is bad, 2 - not bad, 3 - average, 4 - good and 5 is excellent)")
f = int(input("Food Rating: (1-5)"))
s = int(input("Service Rating: (1-5)"))
a = int(input("Ambience Rating: (1-5)"))
bill = int(input("Enter Bill amount: "))

if(f==5 or f==4):
    if(s==5 or s==4 and a==5 or a==4):
        print("Tip is ",(0.1*bill))
    else:
        print("Tip is ", (0.05 * bill))
else:
    if (s == 5 or s == 4 and a == 5 or a == 4):
        print("Tip is ", (0.05 * bill))
    else:
        print("Tip is ", (0.01 * bill))