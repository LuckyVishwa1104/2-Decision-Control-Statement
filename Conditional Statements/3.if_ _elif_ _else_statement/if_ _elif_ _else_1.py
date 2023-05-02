#3. if_ _elif_ _else statement.
# there can be any no. of elif block and else is optional.
'''elif = else if
syntax:
	if (condition):
		statement_n
	elif (condotion):
		statement_n
	else:
		ststement_n
'''
#1. even odd no.
print("even odd no.")
a=eval(input("Enter no. : "))
# check the if codition.
if a%2==0:
	print(a,"is even no.")
# check elif condition
elif a%2==1:
	print(a,"is odd no.")
# otherwise print else block.
else:
	print("Enter valid no.")
#2. positive, negative, zero no.
print("positive, negative, zero no.")
a=float(input("Enter no.: "))
# check the if condition
if a>0:
	print(a,"is positive no.")
# check elif condition
elif a<0:
	print(a,"is negative no.")
# otherwise print else block.
else:
	print("entered no. is zero")