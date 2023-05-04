# range function - generates a sequence of numbers.
''' Syntax:
	  range(initial,final,step-size)
	  initial - starting value
	  final - ending value
	  step-size - fixed difference
	  
range value = int, bin, oct, hex, bool, variable, expression
	'''
#1. range(1,n) - always generates sequence from 1 to   n-1

#2. generates sequence from 0 to 9.        (10 digits)
a=range(0,10)
print(list(a))
a_=range(3,10)
print(list(a_))

#3. if no initial value assigned 0 is taken as default
b=range(10)
print(list(b))
o=range(20)
print(set(o))

#4. if step size not assigned it is taken as 1 by default.
b_=range(1,10)
print(list(b_))

#5. each element increased by 2
c=range(0,11,2)
print(tuple(c))
d=range(0,-11,-2)
print(set(d))



