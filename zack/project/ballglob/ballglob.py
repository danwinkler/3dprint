from solid import *
import random
import sys
from math import *
from random import *

sys.path.append( "../../../" )
from zack.lib.mat import *
from zack.lib.pathmat import *

# A path is a set of points in 3 space
def attenuatedSprial():
	path = []
	steps = 100
	for i in range(0,steps):
		fi = float(i) / float(steps)
		t = 3.14 * 8 * fi
		q = 12 * fi
		p = 500 * exp( -pow(0.3*(q-6),2) )
		v = Vec3( [ p*cos(t), p*sin(t), 2*p ] )
		#v = Vec3( [ 1000 * fi, p, 0 ] )
		path.append( v )
	return path


			

balls = []

path = attenuatedSprial()
#path = [ Vec3([0,0,0]), Vec3([1,1,0]), Vec3([2,1,0]), Vec3([3,1,0]) ]

pathMat = pathToPathMat( path )
steps = 200
for i in xrange( 0, steps ):
	p = i / float(steps)
	v = interpolate( p, pathMat )
	
	trans = Vec3( v.getTrans() )
	offset = Vec3( [ v.m[0][1], v.m[1][1], v.m[2][1] ] )
	offset.mul( 40*gauss(0,1) )
	offset.add( trans )

	balls.append( translate(offset.list())( sphere( uniform(20,100) ) ) )


scad_render_to_file(
	union()( balls ), "ballglob.scad"
)


