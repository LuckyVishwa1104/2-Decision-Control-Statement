#3. greatest among the three no.
#enter three no respectively
a=int(input("enter no._1: "))
b=int(input("enter no_2: "))
c=int(input("enter no_3: "))
#check if condition
if (a>b)and(a>c):
	print(a,"is the greatest no.")
# check elif condition
elif (b>a)and(b>c):
	print(b,"is the greatest no.")
# else print else-block
else:
	print(c,"is greatest no.")