# program to display the result of student
# enter the percentage obtained by student.
marks=float(input("Enter your percentage : "))
# outer if-else statement.
if marks>=40:
	print("congratulations you are passed")
	# nested if_elif_else statement.
	if marks>=85:
		print("first class distinction")
	elif marks>=70:
		print("second class distinction")
	elif marks>=60:
		print("third class distinction")
	elif marks>=50:
		print("on the verge distinction")
	elif marks>=40:
		print("on the edge of passing")
	else:
		print("keep it on !!!")
# else print failed status
else:
	print("you are failed")
	print("try hard next time")
