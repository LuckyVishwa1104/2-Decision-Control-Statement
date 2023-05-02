# greatest and smallest among three no.
# input three numbers.
a=eval(input("Enter first no: "))
b=eval(input("Enter second no: "))
c=eval(input("Enter third no: "))
#1. greatest no.
#outer if_else statement.
if a>b:
	# nested if_else statement
	if a>c:
		print(a,"is the greatest no.")
	else:
		print(c,"is the greatest no.")
else: # b>a.
	if b>c:
		print(b,"is the greatest no.")
	else:
		print(c,"is the greatest no.")
		
#2. smallest no.
# outer if_else statement.
if a<b:
	# nested if_else
	if a<c:
		print(a,"is the smallest no.")
	else:
		print(c,"is the smalleat no.")
else: # b<a
	if b<c:
		print(b,"is the smallest no.")
	else:
		print(c,"is the smallest no.")
	
	