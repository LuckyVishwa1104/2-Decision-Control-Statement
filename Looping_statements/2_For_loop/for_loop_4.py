#4.  program to check whether entered number i s prime or not.
# take the number as input.

n=int(input("enter number : "))
if n>1:
	# using for loop
	for i in range(2,n):
		# nested if-else ststement
		# of the no. having more than one factor.
		if n%i==0:
			print(n,"is not a prime no.")
			break
		else:
			print(n,"is a prime no")
			break
else:
	print(n,"is not prime number")