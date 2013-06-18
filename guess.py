import random

print "Hi! What's your name?"

name = raw_input()

print "%s, I'm thinking of a number between 1 and 100. Try to guess my number!" % name


rand_num = random.randint(1,100)


count = 0
status = True
while status:
	
	print "Your guess?"
	guess = int(raw_input())
	count += 1
	
	if guess < rand_num:
		print "Your guess is too low, try again"
	elif guess > rand_num:
		print "Your guess is too high, try again"
	else:
		print "Well done, %s! You found my number in %d tries!" % (name,count)
		status = False
		 