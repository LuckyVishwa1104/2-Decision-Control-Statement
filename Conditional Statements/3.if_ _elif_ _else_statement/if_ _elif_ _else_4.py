#4. program to input 5 subject marks and display the result accordingly.
# input the marks obtained in each subject
print("Enter marks obtained in each subject out of 100")
s1=float(input("Subject_1 : "))
s2=float(input("Subject_2 : "))
s3=float(input("Subject_3 : "))
s4=float(input("Subjest_4 : "))
s5=float(input("Subject_5 : "))
#calculate total and percentage
total=s1+s2+s3+s4+s5
avg=total/5
print('''Total marks obtained is {0} out of 500.
Average {1} marks obtained in each subject.'''.format(total,avg))
per=(total*100)/500
print("Percentage =",per)
# print the grade obtained.
# check the condition and print the appropriete remark.
if per>85:
	print("you have been passed with Distinction")
elif per>75:
	print("you have been passed with First class")
elif per>60:
	print("you have been passed with Second class")
elif per>40:
	print("you have been passed with Third class")
else:
	print('''you have been FAILED
try your best next time.''')