
##import urllib2
##for line in urllib2.urlopen('http://ipv6.google.com.hk/'):
##    if 'google' in line or 'EDT' in line:  # look for Eastern Time
##        print line

from string import Template
import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'
fmt = raw_input('Enter rename style (%d-date %n-seqnum %f-format):  ')
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print '{0} --> {1}'.format(filename, newname)


