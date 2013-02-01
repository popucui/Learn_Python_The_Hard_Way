import sys

##try:
##    f = open('E:\py\myfile.txt')
##    s = f.readline()
##    i = int(s.strip())
##    print i
##except IOError as e:
##    print "I/O error({0}): {1}".format(e.errno, e.strerror)
##except ValueError:
##    print "Could not convert data to an integer."
##except:
##    print "Unexpected error:", sys.exc_info()[0]
##    raise

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()
