import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

parts = []

w1 = 10
w2 = 22
w3 = 20

h1 = 10
h2 = 20
h3 = 54
h4 = 80

thickness = 5
stem_rad = 5

hole_depth = 10
hole_size = 3 + .5 #.5 so that the 3 rad connector can fit

outline = polygon( points=[[w1,h1], [w2,h2], [w3,h3], [0,h4], [-w3, h3], [-w2, h2], [-w1, h1]] )

parts.append(
    translate( [0, thickness/2.0, 0] ) (
        rotate( v=[1,0,0], a=90 ) (
            linear_extrude(height=5)( outline )
        )
    )
)

parts.append(
    cylinder( r1=stem_rad, r2=1, h=h4-2 ) - cylinder( r=3, h=hole_depth )
)

print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
    f.write( scad_render( union() ( parts ) ) )
