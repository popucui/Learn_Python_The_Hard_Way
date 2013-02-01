the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'aprocots']
change = [1, 'pennies', 2, '']

for num in the_count:
	print "This is count %d" % num

for fruit in fruits:
	print "A fruit of type: %s" % fruit

for i in change:
	print "I got %r" % i
# we can directly use elements to hold the elements range() generate
elements = range(6)
for i in elements:
	 print "Elements was: %d" % i
