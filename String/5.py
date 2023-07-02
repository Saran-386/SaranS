mail = input("Enter your email id: ")
user = mail.split("@")
r = user[0]
p1 = r[::-1]
p2 = p1.upper()
password = r+p2
print("The username is ",user)
print("The password is ",password)