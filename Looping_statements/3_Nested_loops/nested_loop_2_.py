#3. pattern to diaplay arrow heah symbol

# input the value of n
n=int(input("enter number : "))

#1. using for loop
# outer loop
for i in range(1,n+1):
	#.nested loop
	for j in range(1,i+1):
		print("©",end="")
	print("")

# outer loop
for k in range(n,1,-1):
	# nested loop
	for l in range(k,1,-1):
		print("©",end="")
	print("")

#2. using while loop.
# outer loop
a=1
while a<=n:
	# nested loop
	b=1
	while b<=a:
		print("©",end="")
		b=b+1
	print("")
	a=a+1

# outer loop
c=n
while c>1:
	# nested loop
	d=1
	while d<c:
		print("©",end="")
		d=d+1
	print("")
	c=c-1

#3. using for / while loop
# first loop
for d in range(1,n+1):
	e=1
	# nested loop
	while e<=d:
		print("©",end="")
		e=e+1
	print("")

# outer loop
for f in range(n-1,0,-1):
	# nested loop
	g=1
	while g<=f:
		print("©",end="")
		g=g+1
	print("")

#4. using while / for loop
# outer loop
h=1
while h<=n:
	# nested loop
	for i in range(1,h+1):
		print("©",end="")
	print("")
	h=h+1

# outer loop
j=n
while j>1:
	# nested loop
	for k in range(1,j):
		print("©",end="")
	print("")
	j=j-1
	


