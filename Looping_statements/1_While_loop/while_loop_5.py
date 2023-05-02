#5.  program to for displaying fibonacci sreies .
# get the input from the user.
n=int(input("Enter the number : "))
# print the first two terms.
n1=0
n2=1
print(n1)
print(n2)
# using while loop.
while n2<n:
	n3=n1+n2
	n1=n2
	n2=n3
	print(n3)
print("end")