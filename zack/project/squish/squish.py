from math import *
from sys import *

print "module squish() {"
print "polygon( points=["

segs = 8
for i in xrange(0,segs):
	o0 = 0.03
	o1 = 0.15
	a0 = 2*pi*(i+0)/segs
	a1 = 2*pi*(i+0.5)/segs
	a2 = 2*pi*(i+1)/segs

	for j in xrange(0,5):
		if j == 0:
			p = [ 3 * cos(a0+o0), 3 * sin(a0+o0) ]
		elif j == 1:
			p = [ 5 * cos(a0-o1), 5 * sin(a0-o1) ]
		elif j == 2:
			p = [ 5 * cos(a1+o1), 5 * sin(a1+o1) ]
		elif j == 3:
			p = [ 3 * cos(a1-o0), 3 * sin(a1-o0) ]
		elif j == 4:
			p = [ 3 * cos(a2+o0), 3 * sin(a2+o0) ]

		stdout.write( str(p) + "," )


for i in xrange(0,segs):
	r0 = 2.8
	r1 = 4.5
	o0 = -0.15
	o1 = -0.06
	a0 = 2*pi*(i+0)/segs
	a1 = 2*pi*(i+0.5)/segs
	a2 = 2*pi*(i+1)/segs

	for j in xrange(0,5):
		if j == 0:
			p = [ r0 * cos(a0-o0), r0 * sin(a0-o0) ]
		elif j == 1:
			p = [ r1 * cos(a0+o1), r1 * sin(a0+o1) ]
		elif j == 2:
			p = [ r1 * cos(a1-o1), r1 * sin(a1-o1) ]
		elif j == 3:
			p = [ r0 * cos(a1+o0), r0 * sin(a1+o0) ]
		elif j == 4:
			p = [ r0 * cos(a2-o0), r0 * sin(a2-o0) ]

		stdout.write( str(p) + "," )


print "], paths=["

print "["
for a in xrange(0,segs*5):
	stdout.write( str(a) + "," )
print "],"

print "["
for a in xrange(0,segs*5):
	stdout.write( str(segs*5+a) + "," )
print "]"



print "]);"
print "}"
