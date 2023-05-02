#if -elif-else_ nested_if-elae.
# program to play rock paper scissor.
# computer takes any random value
from random import randint
t=["rock","paper","scissor"]
com=t[randint(0,2)]
# enter the choice of the player
pla=input("Enter your choice : ")
print("computer=",com)
# oiter if_elif_else.
if com==pla:
	print("Tie")
elif pla=="rock":
	# nested of_else
	if com=="paper":
		print("you lose")
	else:
		print("you win")
elif pla=="paper":
	# nested if_else
	if com=="rock":
		print("you win")
	else:
		print("you loos")
elif pla=="scissor":
	# nested if_else.
	if com=="paper":
		print("you win")
	else:
		print("you loos")
else:
	print("enter either rock,paper or scissor")
