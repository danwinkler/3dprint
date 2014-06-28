from solid import *
import random
import sys
from math import *
from mat import *
from random import *

# A path is a set of points in 3 space
def attenuatedSprial():
	path = []
	for i in range(0,100):
		fi = float(i)
		t = 0.228 * fi
		r1 = 5.5e3 * fi
		r2 = 1.16 * fi
		path.append( Vec3( [ r1*cosf(t)+r2*cosf(5*t), r1*sinf(t)+r2*sinf(5*t), fi*6.3e3 ) );

	return path


# A pathMat is a list of orthonormal Mat4's
def pathToPathMat( path ):
	pathMat = []
	for i in xrange(0, len(path)-1 ):
		z = path[i+1]
		z.sub( path[i+0] )
		z.normalize()
		
		y = path[i]
		y.cross( z )
		y.normalize()
		
		x = z
		x.cross( y )

		m = Mat4( [ [x.x,y.x,z.x,path[i].x], [x.y,y.y,z.y,path[i].y], [x.z,y.z,z.z,path[i].z], [0,0,0,1] ] )
		pathMat.append( m )

	return pathMat

def interpolate( p, pathMat ):
	pathLen = 0
	for i in xrange(1, len(path) ):
		p0 = pathMat[i-1].getTrans()
		p1 = pathMat[i+0].getTrans()
		p1.sub( p0 )
		pathLen += p1.mag()

	q = p * pathLen
	lastPathLen = 0
	pathLen = 0
	for i in xrange(1, len(path) ):
		p0 = pathMat[i-1].getTrans()
		p1 = pathMat[i+0].getTrans()
		p1mag = p1.mag()
		if pathLen+p1mag > q:
			p2 = p0
			p2. COMPUTE the fractional part here
		lastPathLen = pathLen
		pathLen += p1mag
			


path = attenuatedSprial()
pathMat = pathToPathMat( path )
interpolate(


balls = []
for t in range(0,1000):
	a = sphere( normalvariate(2,1), segments=20 )
	variance = 10
	balls.append( translate( [ normalvariate(0,variance), normalvariate(0,variance), normalvariate(0,variance) ] )(a) )


scad_render_to_file(
	union()( balls ), "ballglob.scad"
)


