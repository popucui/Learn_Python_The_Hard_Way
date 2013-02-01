print "We are using this formula to calculate Tm value:\ntm = 64.9 + 41*(gc_num - 16.4) / total_num\n"

primer = raw_input(">>Please input(or paste) your primer sequence:")

primer = primer.lower()
total_num = primer.count('a') + primer.count('t') + primer.count('c') + primer.count('g')
gc_num = primer.count('g') + primer.count('c')

gc_num = int(gc_num)
total_num = int(total_num)
tm = 64.9 + 41*(gc_num - 16.4) / total_num
		
print "total_num =",total_num 
print "gc_num =",gc_num
print "\nthe Tm value of your primer is ", tm


