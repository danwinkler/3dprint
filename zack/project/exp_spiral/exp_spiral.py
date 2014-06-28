from solid import *
import random
import sys
from math import *

sys.path.append( "../../../" )
from zack.lib.mat import *

def flip( t ):
	x = t[0]
	y = t[1]
	z = t[2]
	return [ z, y, x ]




rot = 3.14*6.0
zn = 60
r2 = 10
r1 = 9
xn = 16
xn2 = xn*2


def deform( z, x, xn, offset ):
	t = rot * float(z)/float(zn)
	r = exp(t*0.1)
	q1 = rotate3D( [1,0,0], -t )
	t1 = trans3D( [ 0, r * cos(t), r * sin(t) ] )
	s1 = scale3D( t )
	t2 = trans3D( [ -float(xn-1)/2.0, 0, 0 ] )
	t3 = trans3D( [ 0, offset, 0 ] )

#	u = 3.14/2.0 * float(x)/float(xn) - 3.14/2.0
#	q2 = rotate3D( [0,0,1], u )

	m = Mat4()
	m.cat( t3 )
#	m.cat( q2 )
	m.cat( q1 )
	m.cat( t1 )
	m.cat( t2 )
	m.cat( s1 )

	return m


points = []
for z in range( 0, zn ):
	for x in range( 0, xn ):
		m = deform( z, x, xn, 0 )

		p1 = m.mul( [ x, 0, 0 ] )
		points.append( p1.list() )

		p1 = m.mul( [ x, 1, 0 ] )
		points.append( p1.list() )


triangles = []

for z in range( 0, zn-1 ):
	for x in range( 0, xn-1 ):
		tri = [ (z+0)*xn2+2*x+2, (z+1)*xn2+2*x+0, (z+0)*xn2+2*x+0 ]
		triangles.append( tri )

		tri = [ (z+1)*xn2+2*x+2, (z+1)*xn2+2*x+0, (z+0)*xn2+2*x+2 ]
		triangles.append( tri )

		tri = [ (z+0)*xn2+2*x+1+0, (z+1)*xn2+2*x+1+0, (z+0)*xn2+2*x+1+2 ]
		triangles.append( tri )

		tri = [ (z+0)*xn2+2*x+1+2, (z+1)*xn2+2*x+1+0, (z+1)*xn2+2*x+1+2 ]
		triangles.append( tri )

for z in range( 0, zn-1 ):
	tri = [ (z+1)*xn2+0, (z+0)*xn2+1, (z+0)*xn2+0 ]
	triangles.append( tri )

	tri = [ (z+0)*xn2+1, (z+1)*xn2+0, (z+1)*xn2+1 ]
	triangles.append( tri )

	tri = [ (z+0)*xn2+xn2-2, (z+0)*xn2+xn2-1, (z+1)*xn2+xn2-1 ]
	triangles.append( tri )

	tri = [ (z+0)*xn2+xn2-2, (z+1)*xn2+xn2-1, (z+1)*xn2+xn2-2 ]
	triangles.append( tri )


z = 0
for x in range( 0, xn-1 ):
	tri = [ (z+0)*xn2+2*(x+1)+1, (z+0)*xn2+2*(x+1)+0, (z+0)*xn2+2*(x+0)+0 ]
	triangles.append( tri )

	tri = [ (z+0)*xn2+2*(x+0)+1, (z+0)*xn2+2*(x+1)+1, (z+0)*xn2+2*(x+0)+0 ]
	triangles.append( tri )

z = zn-1
for x in range( 0, xn-1 ):
	tri = [ (z+0)*xn2+2*(x+0)+0, (z+0)*xn2+2*(x+1)+0, (z+0)*xn2+2*(x+1)+1 ]
	triangles.append( tri )

	tri = [ (z+0)*xn2+2*(x+0)+0, (z+0)*xn2+2*(x+1)+1, (z+0)*xn2+2*(x+0)+1 ]
	triangles.append( tri )



a = polyhedron( points=points, triangles=triangles )

h = hull() (
	translate([-1,0,0])( sphere(0.1) ),
	translate([1,0,0])( sphere(0.1) ),
	translate([0,0,1])( sphere(0.1) ),
	translate([0,1,1])( sphere(0.1) )
)

#feathers = []
#for z in range( 0, zn-1 ):
#	for x in range( 1, xn-2 ):
#		m = deform( z, x, xn-2, 1 )
#		m.cat( trans3D( [ x, 0, 0 ] ) )
#		feathers.append( multmatrix( m.m )( h ) )

#wedges = []
#for z in range( 0, zn-1 ):
#	t = trans3D( [ 0, 2.7*z+9, -0.3 ] )
#	r = rotate3D( [1,0,0], -rot*float(z)/float(zn)-0.1 )
#	s1 = scale3D( [ 1+0.3*z, 1+0.3*z, 1+0.3*z ] )
#	s2 = scale3D( [ 0.25, 0.3, 0.25 ] )
#
#	m = Mat4()
#	m.cat( s1 )
#	m.cat( s2 )
#	m.cat( t )
#	m.cat( r )
#
#	wedges.append( multmatrix( m.m )( h ) )


#c = difference()(
#	union()(
#		a,
#		feathers
#	),
#	wedges
#)

scad_render_to_file(
	difference()(
		a,
		translate([80,-100,-200])(
			cube( [100,300,300] )
		)
	),
	"exp_spiral.scad"
)


