mail = input("Enter your email id: ")
u = mail.split("@")
user = u[0]
r = u[0]
p1 = r[::-1]
p2 = p1.upper()
password = r+p2
print("The username is ",user)
print("The password is ",password)