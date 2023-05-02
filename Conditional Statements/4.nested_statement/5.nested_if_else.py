# program for taking a book from library.
print("have you returned the previous taken book")
# enter your answer in yes or no
ans=input("enter yes/no : ")
# outer if else statement.
if ans=="yes":
	print("you can take the books from library")
	print("which book do you want")
	# entet the name of the book
	bk=input("enter book name: ")
	# nested if else
	if bk=="maths":
		print("oh ! sorry but maths book is currently not available")
	else:
		print("wait for few minutes")
else:
	print("first return the taken book then only you are able to take another books.")
	