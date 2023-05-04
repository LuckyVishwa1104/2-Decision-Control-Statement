# example_3
# using while loop
i=1
while i<=7:
	# conditional if 
	if i>=5:
		print(i,"o'clock Good evening")
		# use of break
		break
	print(i,"o'clock  Good Afternoon")
	i=i+1
	
# example_4
# break with for loop
for j in range(1,11):
	# nested loop
	for i in range(1,11):
		# break with condition
		if i==5:
			break
		print(i,end="  ")
	