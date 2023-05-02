# program for eligibility for vaccine.
# input the age of person.
age=int(input("Enter your age : "))
# check the condition of vaccination.
if age in range(18,125):
	print("You are eligible for Vaccination")
	print('''you can take either one of the vaccine.
Covi-shield or Co-vaccine''')
else:
	print('''you are not eligible for vaccine.
maintain proper distance and periodically sanitise your hands''')