def sphere(r):
    sa=3.14*4*r*r
    vol=(4/3)*3.14*r*r*r
    print("Surface Area is: ",sa)
    print("Volume is: ",vol)

def cylin(r,h):
    sa=(2*3.14*r*r)+2*3.14*r*h
    vol=3.14*r*r*h
    print("Surface Area is: ",sa)
    print("Volume is: ",vol)

def cone(r,h,s):
    sa=(3.14*s)+(3.14*r*r)
    vol=1/3*(3.14*r*r*h)
    print("Surface Area is: ",sa)
    print("Volume is: ",vol)

def rec(l,b,h):
    sa=2((l*b)+(l*h)+(h*b))
    vol=l*b*h
    print("Surface Area is: ",sa)
    print("Volume is: ",vol)

def tri(l,b,h,s):
    sa=b*h + 2*l*s + l*b
    vol=1/2*(l*b)*h
    print("Surface Area is: ",sa)
    print("Volume is: ",vol)

print("1. Sphere /n 2. Cylinder /n 3. Cone /n 4. Rectagular prism /n 5. Triangular prism /n 0. Exit /n")
ch=int(input("Enter choice: "))
while ch!=0:
    if (ch==1):
        r=int(input("Enter radius: "))
        sphere(r)
        break
    elif (ch==2):
        r=int(input("Enter radius: "))
        h=int(input("Enter height: "))
        cylin(r,h)
        break
    elif (ch==3):
        r=int(input("Enter radius: "))
        h=int(input("Enter height: "))
        s=int(input("Enter slant height: "))
        cone(r,h,s)
        break
    elif (ch==4):
        l=int(input("Enter length: "))
        b=int(input("Enter breadth: "))
        h=int(input("Enter height: "))
        rec(l,b,h)
        break
    elif (ch==5):
        l=int(input("Enter length: "))
        b=int(input("Enter breadth: "))
        h=int(input("Enter height: "))
        s=int(input("Enter slant height: "))
        tri(l,b,h,s)
        break
    else:
        break