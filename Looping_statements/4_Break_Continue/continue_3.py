#5. demonstration of continue 
# initial value of i
i=0

while i<10: # while loop
# incerment of i
	i=i+1
	if i==5:
		print("i =",i)
		print(i,"th execution is terminated")
		continue # continue with if 
	print("i =",i)
	print(i,"th execution")
# stop the iteration
print("Final execution")