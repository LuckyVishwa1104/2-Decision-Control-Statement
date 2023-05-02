#3. use of pass with loop
fac=1
# for loop
for i in range(1,11):
	# calculating factorial
	fac=fac*i
	pass # pass 
	if i==1:
		print(i,end=" ")
		continue		
	print("×",i,end=" ")
# display the result
print("=",fac)
print("end")
#4. pass with while loop
# initial value
sm=0
i=1
# while loop
while i<=10:
	sm=sm+i
	if i==1:
		print(i,end=" ")
	i=i+1
	pass  # pass as null statement
	print("+",i,end=" ")
	pass # 2 nd pass 
# display the result
print("=",sm)
print("terminated")
