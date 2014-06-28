from solid import *
import random
import sys
import math

def gen_diffuse(max_t):
	s = []
	x = 0
	for i in xrange(0,max_t):
		s.append( x )
		x += random.normalvariate(0,1)
	return s

def diffuse_traces(steps,num_traces,max_t):
	parts = []

	for t in xrange(0,num_traces):
		sp = []
		for i in xrange(1,max_t):
			_x = steps[0][i-1]
			_y = steps[1][i-1]
			_z = steps[2][i-1]
			x = steps[0][i]
			y = steps[1][i]
			z = steps[2][i]
			sp.append( hull()( translate( [x,y,z] )( sphere( 0.5 ) ), translate( [_x,_y,_z] )( sphere( 0.5 ) ) ) )

		parts.append( union()( sp ) )

	return union()( parts )

num_steps = 1000
steps = []
steps.append( gen_diffuse( num_steps ) )
steps.append( gen_diffuse( num_steps ) )
steps.append( gen_diffuse( num_steps ) )

num_traces = 20
parts = []
parts.append( translate([  0,0,0])( diffuse_traces( steps, num_traces, int(num_steps*0.1) ) ) )
parts.append( translate([50,0,0])( diffuse_traces( steps, num_traces, int(num_steps*0.5 ) ) ) )
parts.append( translate([100,0,0])( diffuse_traces( steps, num_traces, int(num_steps*1.0 ) ) ) )

scad_render_to_file( union()(parts), "diffuse.scad" )


