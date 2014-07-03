from solid import *
import random
import sys
from math import *
from random import *

sys.path.append( "../../../" )
from zack.lib.mat import *
from zack.lib.pathmat import *



def integrateForces():
	dt = 1
	path = []
	vel = Vec3( [ uniform(-3,3), 0,  uniform(20,30) ] )
	pos = Vec3()

	steps = 32
	xf = uniform( 5, 10 ) / float(steps)
	yf = 0
	for i in xrange(steps):
		if i > steps/2:
			force = Vec3( [ 10*xf, yf, 0 ] )
		else:
			force = Vec3( [ xf, yf, 0 ] )
		force.mul( dt )
		vel.add( force )
		velDt = Vec3( vel )
		velDt.mul( dt )
		pos.add( velDt )
		path.append( Vec3(pos) )

	return path

def arc():
	path = []
	for i in xrange(0,16):
		t = 3.14 * 0.5 * float(i) / 16.0
		path.append( Vec3( [ 20 * cos(t), 20 *sin(t), 0 ] ) )
	return path


tubes = []
flowers = []
for i in xrange(0,8):

	path = integrateForces()
	pathMat = pathToPathMat( path )
	tubes.append( extrudeTubeAlongPath( 16, len(pathMat), pathMat, 5 ) )

	p = 0.5
	while p < 0.9:
		m = interpolate( p, pathMat ) 

		length = uniform( 10, 15 )
		width = uniform( 6, 10 )
		depth = uniform( 6, 10 )

		n = Mat4( scale3D( [ length, width, depth ] ) )
		n.cat( trans3D( [length,0,0] ) )
		n.cat( rotate3D( [0,1,0], uniform(0,3.14*0.1) ) )
		if uniform(0,1) < 0.5:
			n.cat( rotate3D( [0,0,1], 3.14) )
		n.cat( m )

		flowers.append(
			multmatrix(n.list())(
				sphere(1,segments=20)
			)
		)

		p += uniform( 0.01, 0.05 )

base = cylinder(r=40,h=30)

balls = []
y = 1
while y < 20:
	for x in xrange(0,20):
		balls.append(
			translate([x*450/20,0,(y-1)*450/20])(
				sphere( r=uniform(2,4), segments=5 )
			)
		)
	y += max( 0.5, 0.1 * y )


frameSize = 500
frameEdge = 40
all = union() (
	scale( [1.9,2.5,1.9] )(
		difference()(
			translate([-frameSize/2,0,0])(
				cube([frameSize,10,frameSize])
			),
			translate([-frameSize/2+frameEdge/2,-5,frameEdge/2])(
				cube([frameSize-frameEdge,10,frameSize-frameEdge])
			),
			translate([-frameSize/2+frameEdge,5,frameEdge])(
				balls
			)
		)
	),
	translate( [-frameSize/3,0,0] )(
		tubes,
		flowers
	)
)


scad_render_to_file(
	all, "bottle_brush.scad"
)


