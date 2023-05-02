#5. basic calculator (+/ - )
# input two number.
num1=eval(input("Enter number 1 : "))
num2=eval(input("Enter number 2 : "))
# diaplay the selection option.
print('''For addition enter- '+'
For subtraction enter- ' - ' ''')
# select the operation type.
ort=input("Enter operation type: ")
# check the condition.
if ort=='+':
	print("Addition is",num1+num2)
elif ort=='-':
	print("Subtraction is",num1-num2)
else:
	print("Enter valid operator.")