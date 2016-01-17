from solid import *
import random
import sys
from math import *
from random import *

sys.path.append( "../../../" )
from zack.lib.mat import *
from zack.lib.pathmat import *

balls = []


steps = 50
for z in xrange( 0, steps ):
	a = uniform(0,2*3.14)
	r = uniform(0,50)
	r *= z * 0.02
	x = r*cos(a)
	y = r*sin(a)
	balls.append(
		translate([x,y,z])( sphere( z*0.2 ) )
	)


u = union() (
	difference() (
		cylinder( 10, 20 ),
		translate([0,0,-1]) (
			cylinder( 4.1, 15+1 ),
		)
	)
)



'''
steps = 50
for i in xrange( 0, steps ):
	a = uniform(0,2*3.14)
	r = uniform(0,50)
	z = uniform(0,+50)
	r *= z * 0.02
	x = r*cos(a)
	y = r*sin(a)

	balls.append(
		translate([x,y,z])( sphere( (z*0.2)+6 ) )
	)

u = union()(
	difference() (
		union() (
			#cylinder( 10, 20 ),
			scale(0.5) (
				translate([0,0,3]) (
					balls
				)
			)
		),
		translate([0,0,-1]) (
			cylinder( 4.1, 15+1 ),
		)
	)
)
'''

scad_render_to_file(
	union()( u ), "wine.scad"
)


