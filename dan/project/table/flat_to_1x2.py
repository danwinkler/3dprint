import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

inner_x = 19
inner_y = 38

height = 40

offset = .15

wall_thickness = 4

angle_in_degrees = 10

z_offset = 10

base_width = 70

support_height = 20
support_length = base_width + 5

parts = []

inner_total_x = inner_x+offset*2
inner_total_y = inner_y+offset*2

cube_x = inner_total_x + wall_thickness*2
cube_y = inner_total_y + wall_thickness*2

hole_size_inner = 1.7

hole = down( wall_thickness ) ( cylinder( r=hole_size_inner, h=wall_thickness*2, segments=12 ) ) + up( wall_thickness-2 ) ( cylinder( r1=hole_size_inner, r2=3, h=2, segments=12 ) )


def cbox( v ):
    return translate( [-v[0]/2.0, -v[1]/2.0, 0] ) (
        cube( v )
    )

head = translate( [0, 0, z_offset] ) (
    rotate( a=45, v=[0,0,1] ) (
        rotate( a=angle_in_degrees, v=[0,1,0] ) (
            cbox( [cube_x, cube_y, height] ) - union() (
                translate( [inner_x*.5+offset, -inner_y*.25, height - 15] ) (
                    rotate( a=90, v=[0, 1, 0] ) (
                        hole
                    )
                ),
                translate( [inner_x*.5+offset, inner_y*.25, height - 15] ) (
                    rotate( a=90, v=[0, 1, 0] ) (
                        hole
                    )
                ),
                translate( [-(inner_x*.5+offset), -inner_y*.25, height - 15] ) (
                    rotate( a=-90, v=[0, 1, 0] ) (
                        hole
                    )
                ),
                translate( [-(inner_x*.5+offset), inner_y*.25, height - 15] ) (
                    rotate( a=-90, v=[0, 1, 0] ) (
                        hole
                    )
                ),
                translate( [0, (inner_y*.5+offset), height - 15] ) (
                    rotate( a=-90, v=[1, 0, 0] ) (
                        hole
                    )
                ),
                translate( [0, -(inner_y*.5+offset), height - 15] ) (
                    rotate( a=90, v=[1, 0, 0] ) (
                        hole
                    )
                )
            )
        )
    )
)

cutaway = translate( [0, 0, z_offset] ) (
    rotate( a=45, v=[0,0,1] ) (
        rotate( a=angle_in_degrees, v=[0,1,0] ) (
            translate( [wall_thickness-cube_x/2.0,wall_thickness-cube_y/2.0,0] ) (
                cube( [inner_total_x, inner_total_y, height+1] )
            )
        )
    )
)

neck_height = z_offset + math.sin( math.radians( angle_in_degrees ) ) * cube_x/2.0
neck_x = math.cos( math.radians( angle_in_degrees ) )  * cube_x

neck = translate( [0, 0, 0] ) (
    rotate( a=45, v=[0,0,1] ) (
        cbox( [neck_x, cube_y, neck_height] )
    )
)

base = cbox( [base_width, base_width, wall_thickness] )
base += rotate( a=45, v=[0,0,1] ) (
    cbox( [base_width, base_width, wall_thickness] )
)

supports = up( wall_thickness ) ( intersection() (
    cbox( [wall_thickness, support_length, support_height] ),
    rotate( a=90, v=[0,1,0] ) (
        down( wall_thickness/2.0 ) (
            scale( [support_height, support_length/2.0, 1] ) ( cylinder( r=1, h=wall_thickness, segments=32 ) )
        )
    )
))

supports += up( wall_thickness ) ( intersection() (
    cbox( [support_length, wall_thickness, support_height] ),
    rotate( a=90, v=[1,0,0] ) (
        down( wall_thickness/2.0 ) (
            scale( [support_length/2.0, support_height, 1] ) ( cylinder( r=1, h=wall_thickness, segments=32 ) )
        )
    )
))

hole_pos = (base_width*.5) - 2
cutaway += rotate( a=45, v=[0,0,1] ) (
    translate( [hole_pos, 0, 0] ) ( hole.copy() ),
    translate( [-hole_pos, 0, 0] ) ( hole.copy() ),
    translate( [0, hole_pos, 0] ) ( hole.copy() ),
    translate( [0, -hole_pos, 0] ) ( hole.copy() ),
)

parts.append( (head + neck + base + supports) - cutaway )

print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
    f.write( scad_render( union() ( parts ) ) )
