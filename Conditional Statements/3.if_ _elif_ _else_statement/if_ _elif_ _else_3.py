#2. currency converter
# selection menu
print('''Dollar to Rupee: enter- 1
Rupee to Dollar: enter- 2''')
# conversion type.
con=int(input("Enter conversion type: "))
# check the conditions.
if con==1:
	d=float(input("Enter dollar: "))
	r=d*63.65
	print(d,"dollar is equal to",r,"rupee")
elif con==2:
	r=float(input("Enter rupee: "))
	d=r/63.65
	print(r,"rupee is equal to",d,"dollar")
else:
	print("Enter valid conversion type.")