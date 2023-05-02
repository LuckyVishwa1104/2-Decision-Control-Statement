#4. nestest conditional statements
'''nested if , nested if_ _else , nested if_ _elid_ _else'''
'''syntax:
	if (condition):
		if (condition):
		    statement_n
	    else:
		    statement_n
   else:
 	    statement_n
'''
#1. comparision of a no.
a=int(input("Enter number : "))
# outer if_ _else statement.
if a != 0:
	# nested if
	if a>0:
		print(a,"is positive number.")
	else:
		print(a,"is negative number.")
else:
	print("entered number is zero.")
#2. user name and pasword.
# enter the user name.
un=input("Enter user name : ")
if un=="phantom":
	print("User name = ",un)
	ps=input("Enter password : ")
	# neted if_ _else
	if ps=="orion":
		print("Password = ",ps)
		print("login succesfully")
	else:
		print("incorrect password")
else:
	print("incorrect username")

