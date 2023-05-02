# Else - can be used with loop when it is not terminated by break.
''' Syntax:
	  loop(condition):
	  	staement-1
	  	--- --- ---
	  	statement_n
	  else:
	  	statement_
	  	--- --- ---
	  rest of code '''
#1. else with while loop
i=1
# while loop
while i<=10:
	print("i =",i)
	i=i+1
# when loop is terminated else is executed
else:
	print("else with while")
print("finished")
#2. else with for loop
# for loop
for i in range(1,11):
	print("i =",i)
# else with for loop
else:
	print("else with for")
print("finished")

'''Such type of else is useful only if there is an if condition present inside the loop which somehow depends on the loop variable.'''	