from solid import *
from random import *
from math import *
import sys
import copy

sys.path.append( "../../../" )
from zack.lib.mat import *
from zack.lib.pathmat import *


class Particle:
	def __init__(self,pos):
		self.pos = copy.deepcopy( pos )
		self.force = Vec3()

particles = []
for i in xrange(0,30):
	pos = Vec3( [uniform(5,6), uniform(5,6), 0.0] )
	particles.append( Particle( pos ) )

def update_particles():
	for i in xrange(0,len(particles)):
		particles[i].force.origin()

	for i in xrange(0,len(particles)):
		a_pos = Vec3( particles[i].pos )
		a_pos.sub( Vec3([5.0,5.0,0.0]) )
		a_pos.mul( 0.001 )
		particles[i].force.sub( a_pos )
		
		for j in xrange(i+1,len(particles)):
			a_pos = Vec3( particles[i].pos )
			b_pos = Vec3( particles[j].pos )
			a_pos.sub( b_pos )
			dist = a_pos.mag()
			if dist > 0.0001 and dist < 2.0:
				a_pos.normalize()
				a_pos.mul( pow( 2.0 - dist, 3 ) )
				particles[i].force.add( a_pos )
				particles[j].force.sub( a_pos )
		

	dt = 0.05
	for i in xrange(0,len(particles)):
		force = Vec3( particles[i].force )
		force.mul( dt )
		particles[i].pos.add( force )


#for i in xrange(0,1000):
#	print i
#	update_particles()

def radial_func( h, height_steps, t, t_steps ):
	t = 3.14*2 * t / float(t_steps)
	radius = float(h+0.5) / float(height_steps) - 0.5
	radius = 10 * radius * radius + 3
	return Vec3( [ radius * cos(t), radius * sin(t), 0 ] )

path = [ Vec3([1,0,0]), Vec3([1,0,5]) ]
path_mat = pathToPathMat( path )
hole = translate([-1,0,0])( extrudeTubeAlongPath( 16, 6, path_mat, 1, radialFunc=radial_func ) )

holes = []
for y in xrange(0,8):
	for x in xrange(0,8):
		_x = 0
		if y % 2 == 0:
			_x = 0.5
		holes.append( translate([8*(x+_x),8*y,-0.1])( hole ) )

sheet = difference()(
	cube( [ 50, 50, 4 ] ),
	holes
)

scad_render_to_file(
	sheet, "sponge.scad"
)


