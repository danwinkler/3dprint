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

hole_depth = 25
connector_length = 45
size = half_in+.5
rad = size/2
wall_thickness = 3

parts = []

#Try to find 2 vectors that are completely clear on one side, prefering one with the largest angle
def find_2_sided_downvec( vec_list ):
	exclude_list = []
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
			return False, False

		#Check for vectors on either side, if one side is clear, that's our side
		def is_clear( vec ):
			for i in xrange( len(vec_list) ):
				if i in big_vec:
					continue
				#angle needs to be >90 (math.pi/2) to make sure its on the other side
				angle = math.acos( vec.dot( vec_list[i] ) )
				if angle < math.pi/2:
					return False
			return True

		cross = vec_list[big_vec[0]].cross( vec_list[big_vec[1]] )
		if is_clear( cross ):
			return True, cross

		#Try other side...
		cross *= -1
		if is_clear( cross ):
			return True, cross

		#Welp this pair is bad, add to exclude_list and try again
		exclude_list.append( big_vec )

def triangle_intersection( v1, v2, v3, o, d ):
	EPSILON = .000001
	#Find vectors for two edges sharing V1
	e1 = v2 - v1
	e2 = v3 - v1
	#Begin calculating determinant - also used to calculate u parameter
	p = d.cross( e2 )
	#if determinant is near zero, ray lies in plane of triangle
	det = e1.dot( p )
	#NOT CULLING
	if det > -EPSILON and det < EPSILON:
		return False;
	inv_det = 1.0 / det;

	#calculate distance from V1 to ray origin
	t = o - v1;

	#Calculate u parameter and test bound
	u = t.dot( p ) * inv_det;
	#The intersection lies outside of the triangle
	if u < 0.0 or u > 1.0:
		return False

	#Prepare to test v parameter
	q = t.cross( e1 );

	#Calculate V parameter and test bound
	v = d.dot( q ) * inv_det;
	#The intersection lies outside of the triangle
	if v < 0.0 or u + v > 1.0:
		return False

	t = e2.dot( q ) * inv_det;

	if t > EPSILON:
		return True

	return False

def find_3_sided_downvec( vec_list ):
	big_down = None
	big_size = 0
	big_shift = 0
	for i in xrange( len(vec_list) ):
		for j in xrange( len(vec_list) ):
			if j == i:
				continue
			for k in xrange( len(vec_list) ):
				if k == i or k == j:
					continue

				v_a = vec_list[j] - vec_list[i]
				v_b = vec_list[k] - vec_list[i]
				v_c = v_a - v_b

				#Check to make sure nobody else is inside triangle
				good = True
				for l in xrange( len(vec_list) ):
					if l in (i, j, k):
						continue

					hit = triangle_intersection( vec_list[i], vec_list[j], vec_list[k], Vec3(), vec_list[l] )
					if hit:
						good = False
						break

				if good:
					#TODO: make this score like the area of the triangle
					score = v_a.length() + v_b.length() + v_c.length()
					if score > big_size:
						big_size = score
						v_b.normalize()
						v_a.normalize()

						big_down = v_b.cross( v_a )
						big_down.normalize()
						if big_down.dot( vec_list[i] ) < 0: #Use the dot to figure out which side I think..
							big_down *= -1

	if big_down != None:
		return True, big_down
	return False, False

def rotate_to( vec, down_vec ):
	vec = vec.copy()
	orig_down = Vec3( .0000001, .0000001, -1 ).normalize()
	axis = orig_down.cross( down_vec )
	dot = orig_down.dot( down_vec )
	angle = math.acos( dot )
	dot2 = abs( dot ) > .5
	if dot > 0 and dot2:
		angle *= -1
	if dot > 0 and not dot2:
		angle *= -1
	if dot < 0 and dot2:
		angle *= -1
	if dot < 0 and not dot2:
		angle *= -1
	return vec.rotate( axis, angle ).normalize()

def build_connector( vec_list, offset ):
	connector = []
	flats = []
	holes = []
	sph = sphere( connector_length )

	for vec in vec_list:
		connector.append( rot_on_vec( vec, cylinder( r=rad+wall_thickness, h=connector_length ) ) )
		holes.append( rot_on_vec( vec, up( connector_length-hole_depth ) ( cylinder( r=rad, h=connector_length ) ) ) )
		flat_angle = -math.degrees( math.atan2( -vec.y, vec.x ) )
		length = Vec3( vec.x, vec.y, 0 ).length()
		flats.append( rotate( v=[0, 0, 1], a=flat_angle ) ( translate( [0, -rad, 0] ) ( cube( [connector_length * length, size, 1] ) ) ) )

	part = hull() ( connector ) #We hull all of the cylinders
	part = intersection() ( part, sph ) #then we intersect with a sphere to round the ends
	part = up( offset ) ( part ) #Shift the part up in prep for the flat hull
	part = hull() ( union() ( flats ) + part ) #We hull with the flat pieces on the xy axis to print easily
	part -= up( offset ) ( holes ) #cut the holes, shifted up because we already shifted the part
	part -= translate( [-100, -100, -100] ) ( cube( [200, 200, 100] ) ) #in case theres a little bit below ground, cut it off

	return part

def connector_redux( vec_list ):
	vec_list = vec_list = [v.copy().normalize() for v in vec_list]

	found, down_vec = find_2_sided_downvec( vec_list )

	if not found:
		found, down_vec = find_3_sided_downvec( vec_list )

	down_vec.normalize()

	if not found:
		print "Couldn't find downvec"

	vec_list = [rotate_to( v, down_vec ) for v in vec_list]

	offset = 1000
	for vec in vec_list:
		if vec.z < offset:
			offset = vec.z

	offset *= connector_length
	offset -= rad + 3
	offset *= -1

	orig_down = Vec3( .0000001, .0000001, -1 ).normalize()
	axis = orig_down.cross( down_vec )
	dot = orig_down.dot( down_vec )
	
	return build_connector( vec_list, offset ) #+ rot_on_vec( down_vec, cylinder(r=1, h=100) )

def connector( vec_list, size_in_inches=half_in ):
	size = size_in_inches+.5
	rad = size / 2.0
	rod_length = 50

	up_vec = Vec3( .000001, .000001, 1 )

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
			found_down_vec = False
			break

		#Check for vectors on either side, if one side is clear, that's our side
		def is_clear( vec ):
			for i in xrange( len(vec_list) ):
				if i in big_vec:
					continue
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
	if not found_down_vec or True:
		big_down = None
		big_size = 0
		big_shift = 0
		for i in xrange( len(vec_list) ):
			for j in xrange( len(vec_list) ):
				if j == i:
					continue
				for k in xrange( len(vec_list) ):
					if k == i or k == j:
						continue

					v_a = vec_list[j] - vec_list[i]
					v_b = vec_list[k] - vec_list[i]
					v_c = v_a - v_b

					#Check to make sure nobody else is inside triangle
					good = True
					for l in xrange( len(vec_list) ):
						if l in (i, j, k):
							continue

						hit = triangle_intersection( vec_list[i], vec_list[j], vec_list[k], Vec3(), vec_list[l] )
						if hit:
							good = False
							break

					if good:
						#TODO: make this score like the area of the triangle
						score = v_a.length() + v_b.length() + v_c.length()
						if score > big_size:
							big_size = score
							#TODO figure out which direction to point
							big_down = v_b.cross( v_a )
							#big_down = v_a.cross( v_b )
							down = Vec3( .000001, .000001, -1 )
							cross = down.cross( big_down )
							angle = math.acos( down.dot( big_down ) )
							a = vec_list[i].rotate( cross, -angle )
							big_shift = a.z*rod_length - rad - 3

		if big_down != None:
			print "found three side"
			down_vec = big_down
			vert_shift = big_shift
			found_down_vec = True

	parts = []
	negs = []
	flats = []

	orig_down = Vec3( .0000001, .0000001, -1 )
	down_vec.normalize()
	down_cross = orig_down.cross( down_vec )
	down_angle = math.acos( orig_down.dot( down_vec ) )

	#transform all vectors
	new_vecs = []
	for v in vec_list:
		new_vecs.append( v.rotate( down_cross, -down_angle ) )

	vec_list = new_vecs
	def rot_helper( cross, angle, obj ):
		return rotate( a=math.degrees( angle ), v=cross.to_list() ) (
			obj
		)

	def rot_final( obj ):
		return obj
		return rotate( a=-math.degrees( down_angle ), v=down_cross.to_list() ) (
			obj
		)

	for v in vec_list:
		cross = up_vec.cross( v )
		angle = math.acos( up_vec.dot( v ) )
		parts.append( rot_helper( cross, angle, cylinder( r=(rad+3), h=rod_length ) ) )
		negs.append( rot_helper( cross, angle, up(25)( cylinder( r=rad, h=100 ) ) ) )

		rot_v = v
		flats.append(
			rotate( v=[0,0,1], a=-math.degrees(math.atan2( -rot_v.y, -rot_v.x )) ) (
				translate( [0, -rad, 0] ) ( cube( [rod_length, size, .1] ) )
			)
		)

	if not found_down_vec:
		flats = []

	part = rot_final( intersection()( hull() ( parts ), sphere( 60 ) ) )
	part += translate( [0, 0, vert_shift if vert_shift != 0 else -(rad + 3)] ) ( union() ( flats ) )
	part -= rot_final( union() ( negs ) )
	#part = rotate( a=-math.degrees( down_angle ), v=down_cross.to_list() ) ( part )

	return part

'''
parts.append( connector([
	Vec3( 0, 0, 1 ),
	Vec3( 1, 0, 1 ),
	Vec3( 0, -1, 1 ),
	Vec3( 0, 1, 0 ),
	Vec3( 1, 0, 0 )
] ) )
'''

if __name__ == "__main__":
	print "Saving File"
	with open( __file__ + ".scad", "w" ) as f:
		f.write( scad_render( union()( parts ) ) )
