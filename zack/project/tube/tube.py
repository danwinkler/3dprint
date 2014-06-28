from math import *
from sys import *


def fn( h, x, y, z ):
	c0 = cos( 3.14 * 0.1 * h )
	s0 = sin( 3.14 * 0.1 * h )
	c1 = cos( 3.14 * 0.0 * h + 3.14/2 )
	s1 = sin( 3.14 * 0.0 * h + 3.14/2 )
	c2 = cos( 3.14 * 0.0 * h + 3.14/2 )
	s2 = sin( 3.14 * 0.0 * h + 3.14/2 )
	c3 = cos( 3.14 * 0.0 * h + 3.14/2 )
	s3 = sin( 3.14 * 0.0 * h + 3.14/2 )

	m11 = c3*c2*c1 - s3*s1
	m21 = -s3*c2*c1 - c3*s1
	m31 = s2*c1
	m41 = 0

	m12 = c3*c2*s1 + s3*c1
	m22 = -s3*c2*s1 + c3*c1
	m32 = s2*s1
	m42 = 0

	m13 = -c3*s2
	m23 = s3*s2
	m33 = c2
	m43 = 0

	m14 = c0 * 5
	m24 = s0 * 5
	m34 = h * 1
	m44 = 1

	_x = m11 * x + m12 * y + m13 * z + m14 * 1
	_y = m21 * x + m22 * y + m23 * z + m24 * 1
	_z = m31 * x + m32 * y + m33 * z + m34 * 1

	return _x, _y, _z


print "polyhedron( points=["

r = 1
hsteps = 100
asteps = 16

for h in xrange(0,hsteps):
	for a in xrange(0,asteps):
		t = 3.14 * 2 * a/asteps
		x = r*cos(t)
		y = r*sin(t)
		z = 0

		x, y, z = fn( h, x, y, z )

		print "[" + str(x) + "," + str(y) + "," + str(z) + "],"



print "], triangles=["

# SIDES

for h in xrange(0,hsteps-1):
	for a in xrange(0,asteps):
		print "[" + str(asteps*h+a) + "," + str(asteps*h+(a+1)%asteps) + "," + str(asteps*(h+1)+a) + "],"
		print "[" + str(asteps*h+(a+1)%asteps) + "," + str(asteps*(h+1)+(a+1)%asteps) + "," + str(asteps*(h+1)+a) + "],"


# END CAPS
for a in xrange(0,asteps-2):
	print "[" + str(0) + "," + str((a+1)%asteps) + "," + str((a+2)%asteps) + "],"
for a in xrange(0,asteps-2):
	print "[" + str((hsteps-1)*asteps) + "," + str((hsteps-1)*asteps+(a+1)%asteps) + "," + str((hsteps-1)*asteps+(a+2)%asteps) + "],"



print "]);"
