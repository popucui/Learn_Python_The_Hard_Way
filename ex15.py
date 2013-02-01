from sys import argv

scirpt, filename = argv
txt = open(filename)
print "Here's your fiule %r:" % filename
print txt.read()
txt.close()
print "I'll also ask you to type it again:"
file_again = raw_input("> ")
print file_again
