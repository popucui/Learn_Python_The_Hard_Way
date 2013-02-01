numbers = []

# def print_num(j, k):
	# i =0
	# while i < j:
		# print "At the top i is %d" % i
		# numbers.append(i)

		# i += k
		# print "Numbers now: ", numbers
		# print "At the bottom i is %d" % i

# print_num(10, 2)
def print_num2(j):
	for i in range(0, j, 2):
		print "At the top i is %d" % i
		numbers.append(i)

		i += 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
print_num2(20)
print "The numbers: "
for num in numbers:
	print num
