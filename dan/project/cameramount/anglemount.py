import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

#Base
part = cube( [24, 24, 3] )

#Vertical part
part += translate( [4, 4, 3] ) (
    union() (
        cube( [16, 16, 12] ),
        translate( [0, 8, 12 ] ) (
            rotate( v=[0, 1, 0], a=90 ) (
                cylinder( r=8, h=16, segments=64 )
            )
        )
    ) - union() (
        #slots
        translate( [3.8, 0, 3.5] ) ( cube( [4.4, 16, 25] ) ),
        translate( [11.8, 0, 3.5] ) ( cube( [4.4, 16, 25] ) ),
        # hole
        translate( [0, 8, 12 ] ) (
            rotate( v=[0, 1, 0], a=90 ) (
                cylinder( r=2.1, h=16, segments=32 )
            )
        )
    )
)

print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
    f.write( scad_render( part ) )
