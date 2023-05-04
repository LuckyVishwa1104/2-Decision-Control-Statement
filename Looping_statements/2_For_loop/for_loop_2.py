#2. program to find sum of n no. by using for loop.

# get the input from user
n=int(input("Enter number : "))
s=0

# using for loop
for i in range(1,n+1):
	# perform the addition
	s=s+i #no need to update the value
print("sum of first",n,"numbers =",s)
print("end")

# program to find factorial of n th no.
n=int(input("Enter number : "))
f=1

# using foor loop
for i in range(1,n+1):
	f=f*i
print("Factorial of",n,"=",f)
print("stop")

