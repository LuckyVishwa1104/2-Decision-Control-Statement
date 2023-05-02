#3. calculate percentage of a student.
#enter the marks obtained in each subject.
print("enter the marks obtained out off 100 in each subject.")
sub1=eval(input("subject 1: "))
sub2=eval(input("subject 2: "))
sub3=eval(input("subject 3: "))
sub4=eval(input("subject 4: "))
sub5=eval(input("subject 5: "))
# calculate total mark obtained.
all_sub=sub1+sub2+sub3+sub4+sub5
# calculate the percentage
per=(all_sub*100)/500
# display whether pass or fail.
print("Percentage =",per)
if per>=35:
	print('''Congratulation !
you have PASSED the semester.''')
else:
	print('''try hard next time?
you are FAILED in this semister.''')
