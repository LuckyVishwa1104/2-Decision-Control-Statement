''' ITERATIVE or LOOPING statements 

used for repeated execution of a block of code'''

'''#1. While loop
until true - while block , false - rest of code

Syntex:
	intial value
	while (condition):
		statement_1
		statement_2
		---  ---   ---
		statement_n
		(increment/decrement)
	
	rest of code.'''
	
print("condition can be of the form of (i in range)")
	
# example 1.
# program to print hello five times

i=1 # initialize value
while i<=5: # condition
	print("hello") # block of code
	i=i+1  # increment or decrement
print("execution ends") # rest of the code

# example 2.
# program to print 1 to 10 digits
i=0
while i<10:
	i=i+1
	print(i)
print("execution end")

# exàmple 3.
# program to print even no. among first n no.
n=int(input("Enter number: "))
i=1
while i<=n:
	if i%2==0:
		print(i)
	i=i+1
print("execution end")

# example 4.
# program to print odd no. among first n no.
n=int(input("Entet number : "))
i=1
while i<=n:
	if i%2!=0:
		print(i)
	i=i+1
print("execution ends")