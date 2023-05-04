#2] Continue - use to break a particular iteration and then continue the loop
# Continue can only be used inside loop or with conditional statement
''' Syntax :
	   loop(condition):
	   	statement_1
	   	continue
	   	statement_n
	   rest of the program'''

# example 1 - continue with while loop
i=0
while i<10:
	i=i+1
	if i==5:
		continue  # continue with conditional
	print(i)
print("execution stopped")

# example 2
# continue with for loop
for i in range(1,21):
	if i%5==0:
		continue # continue with conditional
	print(i,end="  ")
print("execution stopped")