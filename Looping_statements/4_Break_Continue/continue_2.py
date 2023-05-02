#3. program to print even no.
# input the value of n
n=int(input("enter number : "))
# continue with for loop
for i in range(1,n+1):
	if i%2!=0:
		continue # continue with conditional
	print(i,end="  ")
print("")
print("execution stopped")
#4. program to display even no. 
# input the value of n
n=int(input("enter number : "))
# continue with while loop
i=1
while i<n:
		i=i+1 # increment should be here
		if i%2==0:
			continue #continue with conditional
		print(i,end="  ")
print("")
print("execution stopped")
		