# 1] Break - use to break the entire iteration at a particular iteration
# break can only be used inside the loop or with conditional statement
''' syntax:
	  loop_structure:
		  statement_1
		  --   --    --
		  statement_n
		  break
	rest of the program '''

# example_1
# break with for loop
for i in range (1,11):
	print(i)
	break # break the iteration
print("iteration stoped here")

# example_2
# break with while loop
i=1
while i<=10:
	print(i)
	# conditional if statement
	if i==5:
		break  # breaking at a condition
	i=i+1
print("end")