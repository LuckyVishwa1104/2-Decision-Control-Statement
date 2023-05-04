#2. program to display multiplication table from 1 to n no.
# input the value of n
n=int(input("enter number : "))

# outer loop
i=1
while i<=n:
	# initial value
	j=1
	
	while j<=10:   # nested loop
	# calculating the table:
		t=i*j
		j=j+1  # increment
		# display the result
		print(i,"×",j,"=",t)
	i=i+1   # increment
	print()
print("end")
	
		