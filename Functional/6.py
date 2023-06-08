def factorial(n):
	if (n==1 or n==0):
		
		return 1
	
	else:
		1/(n * factorial(n - 1))
		return ()

num = int(input("N = "));
print("number : ",num)
print("Factorial : ",factorial(num))
