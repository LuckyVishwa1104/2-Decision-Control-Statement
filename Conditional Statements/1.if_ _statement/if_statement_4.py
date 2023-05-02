#4. program to display greetung message
# enter the time:
t=int(input("enter time std : "))
# for night
if t in range(1,7):
	print("Good night")
# for morning
if t in range(6,13):
	print("Good morning")
# for afternoon
if t in range(12,18):
	print("Good afternoon")
# for evening
if t in range(19,22):
	print("Good evening")