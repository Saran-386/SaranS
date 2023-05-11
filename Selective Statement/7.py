sal = int(input("Enter your salary: "))
ys = int(input("Enter your year of service: "))

if(ys>10):
    c=sal +(0.1*sal)
    print("your bonus is, ",c)
elif(ys>6 and ys<10):
    c = sal + (0.08 * sal)
    print("your bonus is, ", c)
elif(ys<6):
    c = sal + (0.05 * sal)
    print("your bonus is, ", c)
else:
    print("bye bye no bonus for u :(")