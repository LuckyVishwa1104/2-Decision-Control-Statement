#4. program to display english  alphabates in ascending form.
n=int(input("enter no between 65 to 91 : "))
i=65

# outer loop
while i<=n:
	j=65

	# nested loop
	while j<=i:
		print(chr(j),end="")
		j=j+1
	print()
	i=i+1
	
print("--")