#2. program for sum and fac of n no. using while loop
# program to find sum of n no.
n=int(input("Enter no. : "))
sum=0
i=1
# using while loop
while i<=n:
	sum=sum+i
	i=i+1
print("Sum of first",n,"numbers is",sum)

# calculating the average
avg=sum/n
print("average = ",avg)

# program to find factorial of n no.
n=int(input("Enter no. : "))
fac=1
i=1

# using while loop
while i<=n:
	fac=fac*i
	i=i+1
print("Factorial of",n,"is",fac)
