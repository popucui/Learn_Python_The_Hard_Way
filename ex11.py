print "How old are you?",
age = raw_input()
print 'How tall are you?',
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (
		age, height, weight)

# here is another form
print 'What\'s your name?',
name = raw_input()
print 'Where are you from?',
sc = raw_input()
print 'What do you do now?',
job = raw_input()

print 'So you are %r, and from %r, and a %r, welcome!' % (
		name, sc, job)
