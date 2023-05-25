def interest_calc(age,g,p,noy):
    if (age<60):
        i=p*(0.12)*noy
        print("Rate of interest is: ",i)
    elif(g=='F'):
        i=p*(0.1)*noy
        print("Rate of interest is: ",i)
    else:
        i=p*(0.09)*noy
        print("Rate of interest is: ",i)



name =input("Enter your name: ")
age = int(input("Enter your age: "))
g = input("Enter your Gender(M/F): ")
p = int(input("Enter principle amt: "))
noy = int(input("Enter the number of years: "))

interest_calc(age,g,p,noy)
