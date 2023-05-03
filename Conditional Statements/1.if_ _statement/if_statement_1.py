''' selection or conditional or branching statement - these are the condition controled statements.
If the condition is true then only the statements will get executed otherwise it will move next construct of program

 1.If statement - if the condition is true then If block will be executed other wise rest of the code is executed is execcuted'''
''' syntax:
	if (condition):
		statement_1
		statement_2
		- - -       - - -
		statement_n
	rest of the code
'''
# condition can be - is an expression which may result in either true or false
#example-1.
if 5<10:
	print("5 is less than 10")

#2. equal to/ not equal to.
if 4==4:
	print("both no. are equal")
if 4 != 5:
	print("4 is not equal to 5")

#3. positive no.
print(" positive and negative")
a=int(input("enter integer value only: "))
if a<0:
	print(a,"is not positive no.")
print(a,"is positive no.")

#4. even no.
print("even and odd")
b=eval(input())
if b%2==0:
	print(b,"is a even no.")
if b%2==1:
	print(b,"is a odd no.")

#5. eligibility for voting
print(" eligibility for voting")
age=int(input("Enter your age : "))
if age in range(18,125):
	print("you are eligible for voting.")
if age in range(0,18):
	print("you are not eligible for voting")
