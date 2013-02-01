print "You enter a dark room with two doors."

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake.what do you do?\n1. Take the cake.\n2.Scream at the bear."

	bear = raw_input("> ")
	if bear == "2":
		print "The bear eats your legs off.Good job!"
	elif bear == "1":
		print "The bear eats your face off. Good job!"
	else:
		print "Well, doing %s is probably better.Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthuhlu's retina."
	print "1.Blueberried.\n2. Yellow jacket clothespins.\n3. Understanding revolvers yelling methodies."
	
	insanity = raw_input("> ")

	if insanity == "1" or  insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muk. Good job!"

elif door == "3":
	print "You stand in front of an elephant."
	print "1. turn around.\n2. move on.\n3. stop there."

	el = raw_input("> ")
	if el == "1":
		print "Ok, you safe!"
	elif el == "2":
		print "you are very brave, good  luck!"
	else:
		print "yuo've got to know this: no risk, no reward!"
else:
	print "You stumble around and fall on a knife and die. Good job!"

