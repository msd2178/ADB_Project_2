__author__ = 'meril'

import urllib
# params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
# print params
# print "================================="
# f = urllib.urlopen("http://www.musi-cal.com/cgi-bin/query?%s" % params)
# print f.read()

print urllib.quote("cat dog mouse")


a = {}
print bool(a)
a = { 'apple' : 'true'}
print bool(a)


