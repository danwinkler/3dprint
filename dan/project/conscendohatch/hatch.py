import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

parts = []

#front hook
parts.append(
	translate( [0, -8.5, 0] ) ( cube( [40,17,9] ) ) -
	translate( [7, -10, 9 ] ) ( rotate( v=[0, 1, 0], a=150 ) ( down( 5 ) ( cube( [20, 20, 5] ) ) ) )
)

#main spar
parts.append(
	translate( [7, -8.5, 9] ) ( cube( [158, 17, 9] ) )
)

#back snap
parts.append(
	translate( [163.5, -4.25, 0] ) ( cube( [1.5, 8.5, 9] ) )
)

#backsnap hook
parts.append(
	translate( [163.5, -4.25, 4.5] ) (
		rotate( v=[1, 0, 0], a=-90 ) (
			linear_extrude( height=8.5 ) ( polygon( points=[[0, 0], [4.5, 2], [1.5, 4.5], [0, 4.5]] ) )
		)
	)
)

parts = up( 18 ) ( rotate( v=[1,0,0], a=180 ) ( parts ) )

print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
	f.write( scad_render( union()( parts ) ) )
