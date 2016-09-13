import sys
sys.path.append( "../../../" )

from dan.lib.helper import *
from dan.lib.premade import *

import math
import random

from solid import *
from solid.utils import *

wall_thickness = 4

offset = .15

inner_x = 19 + offset*2
inner_y = 38 + offset*2

length = 60

lip_size = 20

outer_x = inner_x + wall_thickness*2
outer_y = inner_y + wall_thickness*2

parts = []

parts += [
    translate( [0,0,0] ) (
        cube( [outer_x, length, outer_x-wall_thickness] ),
        hole() (
            translate( [wall_thickness, -1, wall_thickness] ) (
                cube( [inner_x, length+2, outer_x+1] )
            )
        ),
        hole() (
            translate( [outer_x*.5, length*.5, 0] ) (
                rotate( a=-180, v=[1,0,0] ) (
                    screwhole( "#8 Wood", wall_thickness+1 )
                )
            )
        )
    ),
    translate( [outer_x, 0, 0] ) (
        cube( [lip_size, length, wall_thickness] )
    ),
    hole() (
        translate( [0, length*.33, outer_x*.5] ) (
            rotate( a=-90, v=[0,1,0] ) (
                screwhole( "#8 Wood", outer_x+1 )
            )
        ),
        translate( [0, length*.66, outer_x*.5] ) (
            rotate( a=-90, v=[0,1,0] ) (
                screwhole( "#8 Wood", outer_x+1 )
            )
        ),
        translate( [outer_x+lip_size*.5, length*.5, 0] ) (
            rotate( a=180, v=[0,1,0] ) (
                screwhole( "#8 Wood", wall_thickness+1 )
            )
        )
    )
]

partsa = [
    hole() (
        translate( [-100, -100, -100] ) (
            cube( [200, 200, 100] )
        ),
        translate( [-100, -100, outer_x-wall_thickness] ) (
            cube( [200, 200, 100] )
        )
    )
]


print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
    f.write( scad_render( union() ( parts ) ) )
