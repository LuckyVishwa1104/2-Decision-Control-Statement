#3. program to check even element in sequence
list=[1,3,5,7,9,17,23]
for i in list:
	# nested if statement
	if i%2==0:
		print("there is one even element in list - ",i)
		break
# else with loop
else:
	print("there is no even element in list")
	
#4. else block with loop
for i in range(1,11):
	pass
	print(i,end=" ")
	if i==7:
		print("")
		print(i,"is nothing different")
		break
# else with for loop
else:
	print("ok, finished")

	