import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

inches_in_mm = 25.4
half_in = inches_in_mm / 2.0

parts = []

#parts.append( cube( [20, 20, 5] ) )

rad = half_in+.5
outer_rad = rad + 5
rad = rad / 2.0
outer_rad = outer_rad/2.0
parts.append( 
	translate( [10, 10, 0] ) (
		cylinder(r=outer_rad, h=25) - up(5)(cylinder(r=rad, h=30)) - translate( [0, -5, 17] ) ( rotate( a=90, v=[1, 0, 0] )( cylinder(r=1.5, h=6, segments=12) ) )
	)
)

print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
	f.write( scad_render( union()( parts ) ) )