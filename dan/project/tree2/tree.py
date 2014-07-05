import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

parts = []


def r_vine():
	points = []

	points.append( Vec3( 0,0,0 ) )

	variance = .3
	z_var = .1
	length = 4

	vec = Vec3( 0, 0, 1 )
	for i in range( 100 ):
		vec.normalize()
		
		vec.x += random.uniform( -variance, variance ) + ((-vec.x ** 3) * 1)
		vec.y += random.uniform( -variance, variance ) + ((-vec.y ** 3) * 1)
		vec.z += random.uniform( -z_var, z_var )
		
		vec *= length
		
		np = points[-1] + vec
		
		points.append( np )
	
	def wf( pi, r ):
		return 4
	
	return vine( points, wf )

for i in range( 10 ):
	parts.append( r_vine() )
	
	
print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
	f.write( scad_render( union()( parts ) ) )