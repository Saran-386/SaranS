name =input("Enter your name: ")
age = int(input("Enter your age: "))
g = input("Enter your Gender(M/F): ")
nod = input("Enter the number of days you're ready to work: ")
if(age>=18 and age<30 and g=='M'):
    print("your total wage will be: ",nod*700)
elif(age>=18 and g=='F'):
    print("your total wage will be: ", nod * 750)
elif(age>=30 and age<40 and g=='M'):
    print("your total wage will be: ", nod * 800)
elif(age>=30 and age<40 and g=='F'):
    print("your total wage will be: ", nod * 800)