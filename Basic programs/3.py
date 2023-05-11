t=int(input("enter a temperature in degree celsius:"))
v =int(input("enter a wind speed kilometers/hour:"))
f=13.12+(0.6215*t-11.37*v**0.16)+(0.3965*t*v**0.16)
print("the calculated a wind speed of chill index in celsius",int(round(f,0)))
