#3. Nested loop - one loop is present inside the other loop.
''' Systtax :
	initial value
	(Outer loop):
		statement_
		{
		initial value
		(Inner loop):
			statement_1
			statement_2
			_ _ _      _ _ _
			statement_n
			increment/decrement
		}
		increment/decrement
	rest of the code'''
	
# program to find factorials of first n no.
# input the value of n
n=int(input("enter number : "))

#1. for loop / for loop.
print("1. for loop >> for loop")
for i in range(1,n+1): # outer loop
	fac=1
	for j in range(1,i+1):# inner loop
		fac=fac*j
	print(i,"! =",fac)
print("end")

#2. for loop / while loop
print("2. for loop >> while loop")
for i in range(1,n+1):  # outer loop
	j=1
	fac=1
	while j<=i:  # inner loop
		fac=fac*j
		j=j+1
	print(i,"! =",fac)
print("end")

#3. while loop / while loop
print("3. while loop >> while loop")
i=1
while i<=n:  # outer loop
	fac=1
	j=1
	while j<=i:  # inner loop
		fac=fac*j
		j=j+1
	print(i,"! =",fac)
	i=i+1
print("end")

#4. while loop / for loop
print("4. while loop >> for loop")
i=1
while i<=n:  # outer loop
	fac=1
	for j in range(1,i+1):   # inner loop
		fac=fac*j
	print(i,"! =",fac)
	i=i+1
print("end")
	