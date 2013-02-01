from sys import argv
script, user_name = argv
prompt = 'your answer here:'
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)

print "Tell me something about your hobby %s" % user_name
hobby = raw_input(prompt)
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where it is.
And you have a %r computer. Also, you like %r\nNice.
""" % (likes, lives, computer, hobby)
