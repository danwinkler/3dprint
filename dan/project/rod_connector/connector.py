import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

#Hole center is 12 mm from base and is 1.5mm radius

inches_in_mm = 25.4
half_in = inches_in_mm / 2.0

parts = []
neg_parts = []

rad = half_in+.5
outer_rad = rad + 5
rad = rad / 2.0
outer_rad = outer_rad/2.0

def connector( vec_list, size_in_inches=half_in ):
	size = size_in_inches+.5
	rad = size / 2.0

	avg = Vec3()
	up_vec = Vec3( 0, 0, 1 )

	for v in vec_list:
		v.normalize()
		avg += v

	avg.normalize()

	a_rot_vec = up_vec.cross( avg )
	a_rot_angle = math.acos( up_vec.dot( avg ) )

	part = sphere( 30 )

	for v in vec_list:
		cross = up_vec.cross( v )
		angle = math.acos( up_vec.dot( v ) )
		part -= rotate( a=-math.degrees( a_rot_angle ), v=a_rot_vec.to_list() ) (
			rotate( a=math.degrees(angle), v=cross.to_list() ) (
				up( 10 ) ( cylinder( r=rad, h=30 ) )
			)
		)

	return part

parts.append( connector([
	Vec3( 0, 0, 1 ),
	Vec3( 1, 0, 1 ),
	Vec3( 0, -1, 1 ),
	Vec3( 0, 1, 0 ),
	Vec3( 1, 0, 0 )
] ) )

'''
def port():
	return translate( [0, 0, 0] ) (
		cylinder(r=outer_rad, h=25)
	)

def port_neg():
	return translate( [0, 0, 0] ) (
		up(5)(cylinder(r=rad, h=30)),
		translate( [0, -5, 17] ) ( rotate( a=90, v=[1, 0, 0] )( cylinder(r=1.5, h=6, segments=12) ) )
	)

def make_port( a, v, r=0 ):
	p = [port()]
	if a == 90 or a == -90:
		p.append( translate( [-outer_rad, -outer_rad, 0] ) ( cube( [outer_rad*2, outer_rad*2, 25] ) ) )
	parts.append(
		rotate( a=a, v=v ) (
			up( 15 ) (
				p
			)
		)
	)

	neg_parts.append(
		rotate( a=a, v=v ) (
			up( 15 ) (
				rotate( a=r, v=[0,0,1] ) (
					port_neg()
				)
			)
		)
	)
parts.append( sphere( r=20 ) - translate( [-100, -100, -100] ) ( cube( [200,200,100] ) ) )

make_port( 45, [0, 1, 0] )
make_port( 0, [0, 1, 0], r=45 )
make_port( 45, [1, 0, 0] )
make_port( -60, [1, 0, 0], r=-90 )
make_port( -90, [0, 1, 0] )

parts.append( down( outer_rad ) ( cylinder( r=20, h=outer_rad ) ) )
'''

print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
	f.write( scad_render( union()( parts ) ) )
