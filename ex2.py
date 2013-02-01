my_name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % height
print "He's %d pouds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "He's teeth are usually %s depending on the coffe." % teeth

# this line is a little tricky
print "If I add %d,%d,and %d I get %d." % (
	age, height, weight, age + height + weight)