#4] Pass - use to define empty block, it does nothing just continue current iteration
# it can also be used outside the loop
''' Syntax:
	loop(condition):
		statement_1
		statement_2
		- - - - 
		pass
		statement_n
	rest of the code '''
#1. print digit 1 to 10 : pass with while loop
i=1
while i<=10:
	print("i =",i)
	pass
	print(i,"th iteration")
	i=i+1
print("execution terminated")

#2. pass with for loop
for i in range(1,11):
	print("i =",i)
	pass
	print(i,"th iteration")
print("execution stopped")
	
	