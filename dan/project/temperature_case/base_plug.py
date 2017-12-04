import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

def pin_holes(n):
    pin_hole_depth = .25
    hole_radius = .02
    return cube([.1, .1*n, pin_hole_depth]) + [
        translate([.05-hole_radius, .05-hole_radius+.1*i, 0]) (
            hole()(cube([hole_radius*2, hole_radius*2, pin_hole_depth+.001]))
        ) for i in range(n)
    ]

parts = []

parts.append(pin_holes(12))
parts.append(cube([.8*in_to_mm, 1.2*in_to_mm, 2]))
parts.append(right(.7*in_to_mm)(pin_holes(12)))

if __name__ == '__main__':
    print( "Saving File" )
    with open( __file__ + ".scad", "w" ) as f:
        f.write( scad_render( union() ( parts ) ) )
