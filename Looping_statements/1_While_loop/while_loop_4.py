#4.program to find whether the number is armstrong or not.
n=int(input("Enter three digit number : "))
m=n
sum=0
# using while loop.
while n>0:
	# to get last digit of n
	t=n%10
	sum=sum+(t**3)
	# to get other than last
	n=n//10
if sum==m:
	print("It is an Armstrong number")
else:
	print("It is not an Armstrong number")

	