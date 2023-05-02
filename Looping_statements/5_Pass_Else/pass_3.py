#5.the prior use of pass is  when we want to implement loop in future
for i in range(1,11):
	pass
i=1
while i<=10:
	pass
	i=i+1
# pass produces an empty block which is considered as for loop block.
# if we dont use pass it will produce error i.e. there must be some block of code when we declare a loop.
# we cant keep an loop empty