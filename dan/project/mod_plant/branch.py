import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

parts = []

stem_rad = 5

hole_depth = 10
hole_size = 2.5

def branch( length, hole=False, nub=True ):
    o = cylinder( r=stem_rad, h=length )
    if nub:
        o += up( length ) ( cylinder( r=hole_size, h=8, segments=36 ) )
    if hole:
        o -= cylinder( r=hole_size, h=hole_depth, segments=36 )
    return o



def typeA():
    o = branch( 150, hole=True )

    for i in range( 4 ):
        o += up( i * 30 + 15 ) (
            rotate( v=[0,0,1], a=(0 if (i%2)==0 else 180) ) (
                rotate( v=[0,1,0], a=45 ) (
                    branch( 40 )
                )
            )
        )

    return o


branch_types = [
    typeA
]

print "Saving File"
for t in branch_types:
    with open( t.__name__ + ".scad", "w" ) as f:
        f.write( scad_render( t() ) )
