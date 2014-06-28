from solid import *
import random
import sys
from math import *
from random import *

sys.path.append( "../../../" )
from zack.lib.mat import *

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


# A pathMat is a list of orthonormal Mat4's
def pathToPathMat( path ):
	pathMat = []
	for i in xrange(0, len(path) ):
		if i == len(path)-1:
			z = Vec3( path[i] )
			z.sub( path[i-1] )
		else:
			z = Vec3( path[i+1] )
			z.sub( path[i] )
		z.normalize()
		
		y = Vec3( path[i] )
		y.cross( z )
		y.normalize()
		
		x = Vec3( z )
		x.cross( y )

		m = Mat4( [ [x.x,y.x,z.x,path[i].x], [x.y,y.y,z.y,path[i].y], [x.z,y.z,z.z,path[i].z], [0,0,0,1] ] )
		pathMat.append( m )

	return pathMat

def interpolate( p, pathMat ):
	totalPathLen = 0
	for i in xrange(1, len(path) ):
		p0 = Vec3( pathMat[i-1].getTrans() )
		p1 = Vec3( pathMat[i+0].getTrans() )
		p1.sub( p0 )
		totalPathLen += p1.mag()

	q = p * totalPathLen

	pathLen = 0
	lastPathLen = 0
	for i in xrange(1, len(path) ):
		p0 = Vec3( pathMat[i-1].getTrans() )
		p1 = Vec3( pathMat[i+0].getTrans() )
		p1.sub( p0 )
		p1mag = p1.mag()
		if pathLen+p1mag > q:
			frac = ( q - lastPathLen ) / p1mag
			p1.mul( frac )
			p2 = Vec3( p0 )
			p2.add( p1 )
			m = Mat4( pathMat[i-1] )
			m.setTrans( p2 )
			return m

		pathLen += p1mag
		lastPathLen = pathLen

	return pathMat[len(path)-1]
			

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


