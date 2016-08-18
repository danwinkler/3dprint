import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

parts = []

r_parts = 6
h_parts = 5

height = 70

def width_fn( r, h ):
    return 20 - h*5

def outer_fn( h, a ):
    a *= math.pi*2
    a += h * math.pi * 2
    rad = width_fn( a, h )
    x = math.cos( a ) * rad
    y = math.sin( a ) * rad
    z = h * height

    return [x,y,z]

def inner_fn( h, a ):
    a *= math.pi*2
    a += h * math.pi * 2
    rad = width_fn( a, h ) - 1
    if( h == 1 ):
        rad -= 3
    x = math.cos( a ) * rad
    y = math.sin( a ) * rad
    z = h * height

    return [x,y,z]

outer = make_trunk( h_parts, r_parts, outer_fn )
outer -= make_trunk( h_parts, r_parts, inner_fn ) - cylinder( r=1000, h=1 )

parts.append( outer )

threads = up( height ) (
    cylinder( r=12, h=10 ) - cylinder( r=10, h=10 )
)

parts.append( threads )

print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
    f.write( scad_render( union() ( parts ) ) )
