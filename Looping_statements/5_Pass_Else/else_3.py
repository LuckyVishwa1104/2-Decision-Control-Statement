#5. program to check whether a no. is prime or not.
# input the number.
n=int(input("Enter number : ")) 
# using while loop
i=2
while i<n:
	# nested if statement.
	if n%i==0:
		print(n,"is Not a Prime no.")
		break
	i=i+1
# elsr with while loop
else:
	print(n,"is a Prime no.")
print("stop")