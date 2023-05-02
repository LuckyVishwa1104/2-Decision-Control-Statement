#5 program to print no. 0 to 9 in the matrix form.
# outer for loop
a=1
for i in range(1,4):
	# nested whe loop
	j=1
	while j<=3:
		# displaying the result
		print(a," ",end="")
		j=j+1  # incrementing
		a=a+1 # increment
	print()
print("--")