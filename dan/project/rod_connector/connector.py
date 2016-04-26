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

def connector( vec_list, size_in_inches=half_in ):
	size = size_in_inches+.5
	rad = size / 2.0

	up_vec = Vec3( 0, 0, 1 )

	vec_list = [v.normalize() for v in vec_list]

	#Find down vector to rotate to by finding the largest angle between two vectors and then
	#Taking the cross product, then checking each direction to make sure it's clear to rotate down from
	#If it's not clear, loop around and try again

	down_vec = Vec3( 0, 0, -1 )
	vert_shift = 0
	found_down_vec = True
	exclude_list = [] #if the pair of vecs isn't clear on either side, try again but don't look at that
	while(True): #while we havent found the vector we want
		big_vec = None
		big_angle = 0
		for i in xrange( len(vec_list) ):
			for j in xrange( i+1, len(vec_list) ): #start at i+1 so that we don't test i,j if we've already tested j,i
				if i == j:
					continue
				if (i,j) in exclude_list:
					continue

				angle = math.acos( vec_list[i].dot( vec_list[j] ) )
				if angle > big_angle:
					big_vec = (i, j)
					big_angle = angle

		#If big_vec == None, we failed to find a flat spot between two vectors
		if big_vec == None:
			print "down_vec calc failed"
			found_down_vec = False
			break

		#Check for vectors on either side, if one side is clear, that's our side
		def is_clear( vec ):
			for i in xrange( len(vec_list) ):
				if i in big_vec:
					pass
				#angle needs to be >90 (math.pi/2) to make sure its on the other side
				angle = math.acos( vec.dot( vec_list[i] ) )
				if angle < math.pi/2:
					return False
			return True

		cross = vec_list[big_vec[0]].cross( vec_list[big_vec[1]] )
		if is_clear( cross ):
			down_vec = cross
			break

		#Try other side...
		cross *= -1
		if is_clear( cross ):
			down_vec = cross
			break

		#Welp this pair is bad, add to exclude_list and try again
		exclude_list.append( big_vec )

	#Okay so we didn't find a flat spot using two vectors. Now we have to find one using three
	big_set = None
	big_size = 0
	for i in xrange( len(vec_list) ):
		for j in xrange( len(vec_list) ):
			if j == i:
				continue
			for k in xrange( len(vec_list) ):
				if k == i or k == j:
					continue

				v_a = vec_list[j] - vec_list[i]
				v_b = vec_list[k] - vec_list[i]

				#Check to make sure nobody else is inside triangle



	parts = []
	negs = []
	flats = []

	def rot_helper( cross, angle, obj ):
		return rotate( a=-math.degrees( angle ), v=cross.to_list() ) (
				obj
			)

	for v in vec_list:
		cross = up_vec.cross( v )
		angle = math.acos( up_vec.dot( v ) )
		parts.append( rot_helper( cross, angle, cylinder( r=rad+3, h=50 ) ) )
		negs.append( rot_helper( cross, angle, up(25)( cylinder( r=rad, h=100 ) ) ) )
		flats.append(
			rotate( v=[0,0,1], a=math.degrees(math.atan2( -v.y, -v.x )) ) (
				translate( [0, -rad, -rad-3 if vert_shift == 0 else vert_shift] ) ( cube( [50, size, .1] ) )
			)
		)

	if not found_down_vec:
		flats = []

	part = intersection()( hull() ( parts + flats ), sphere( 60 ) ) - union() ( negs ) + flats
	orig_down = Vec3( 0, 0, -1 )
	down_cross = orig_down.cross( down_vec )
	down_angle = math.acos( orig_down.dot( down_vec ) )
	part = rotate( a=math.degrees( down_angle ), v=down_cross.to_list() ) ( part )
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

if __name__ == "__main__":
	print "Saving File"
	with open( __file__ + ".scad", "w" ) as f:
		f.write( scad_render( union()( parts ) ) )
