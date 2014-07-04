import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

parts = []

points = []
widths = []

points.append( Vec3( 0,0,0 ) )
widths.append( 10 )

variance = .5

vec = Vec3( 0, 0, 1 )
for i in range( 100 ):
	np = points[-1] + vec
	widths.append( 10 )
	
	points.append( np )
	
	vec.x += random.uniform( -variance, variance )
	vec.y += random.uniform( -variance, variance )
	vec.z += random.uniform( -variance, variance )
	
	vec.normalize()

cross = points[0].copy()
cross.x += random.uniform( -.5, .5 )
cross.y += random.uniform( -.5, .5 )
cross.z += random.uniform( -.5, .5 )
	
def tf( h, a ):
	global cross
	if h == 0:
		vec = points[1] - points[0]
	elif h == len(points)-1:
		vec = points[-1] - points[-2]
	else:
		vec = (points[h] - points[h-1]) + (points[h+1] - points[h])
	
	vec.normalize()
	
	angle = (a/8.0) * math.pi * 2
	
	#cvec = Vec3( math.cos( angle ), math.sin( angle ), 0 )
	
	p = vec.cross( cross )
	
	p = p.cross( vec )
	
	cross = p
	cross.normalize()
	
	p = p.rotate( vec, angle )
	
	return [points[h].x + p.x, points[h].y + p.y, points[h].z + p.z]
		
	
parts.append( make_trunk( len( points ), 8, tf, index=True ) )
	
	
print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
	f.write( scad_render( union()( parts ) ) )