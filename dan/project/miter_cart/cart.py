import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

from wood import *

mm_to_in = 25.4

#Cart variables
platform_width = 26
cart_width = platform_width + (5.5-1.5) * 2
cart_depth = 24
cart_height = 36
shelf_height_above_ground = 4
wing_height = 5
wing_width = 24

wing_lifted = True

parts = []

def bottom_shelf():
    shelf_width = cart_width - 1.5 * 4
    shelf_depth = cart_depth - 1.5 * 4
    shelf = [
        #Front
        wood_2x4( shelf_width ),
        #Back
        translate( [0, shelf_depth - 1.5, 0 ] ) (
            wood_2x4( shelf_width )
        ),
        #Left
        translate( [0, 1.5, 0] ) (
            cube_rot( [0, 2, 1] ) (
                wood_2x4( shelf_depth-1.5*2 )
            )
        ),
        #Right
        translate( [shelf_width-1.5, 1.5, 0] ) (
            cube_rot( [0, 2, 1] ) (
                wood_2x4( shelf_depth-1.5*2 )
            )
        ),
        #shelf
        translate( [0, 0, 3.5] ) (
            plywood( shelf_width, shelf_depth )
        )
    ]
    return shelf

def leg():
    leg_board_length = cart_height - shelf_height_above_ground - .5
    return [
        cube_rot( [1, 0, 2] ) (
            wood_2x6( leg_board_length )
        ),
        translate( [0, 1.5, 0] ) (
            cube_rot( [0, 1, 2] ) (
                wood_2x4( leg_board_length )
            )
        ),
        down( 1.5 ) (
            cube_rot( [1, 2, 0] ) (
                wood_2x6( 5.5 )
            )
        )
    ]

def pins( depth=3.5 ):
    num_holes = 4
    hole_margin = 3.5
    holes_depth = cart_depth - (hole_margin*2)
    holes_sep = holes_depth / (num_holes-1)
    return [
        translate( [1.5 * .5 - (1.5 if n == 1 or n == 2 else 0), hole_margin + n * holes_sep, 0] ) (
            cylinder( r=.4, h=depth, segments=8 )
        )
        for n in range( num_holes )
    ]

def rim():
    def side():
        return union()(translate( [0, 1.5, 0 ] ) (
            cube_rot( [0, 2, 1] ) (
                wood_2x4( cart_depth - 1.5*2 )
            )
        ) + translate( [1.5, 1.5 + 1.5 + 3.5, 0 ] ) (
            cube_rot( [0, 2, 1] ) (
                wood_2x4( cart_depth - 1.5*4 - 3.5*2 )
            )
        ) + translate( [3, 1.5 + 1.5, 0 ] ) (
            cube_rot( [0, 2, 1] ) (
                wood_2x4( cart_depth - 1.5*4 )
            )
        )) - translate( [1.5, 0, -.1] ) (
            scale( [-1, 1, 1] ) (
                pins( 3.7 )
            )
        )

    return [
        wood_2x4( cart_width ),
        translate( [0, cart_depth-1.5, 0] ) (
            wood_2x4( cart_width )
        ),
        #Left
        side(),
        #Right
        translate( [cart_width, 0, 0] ) (
            scale( [-1, 1, 1] ) (
                side()
            )
        )
    ]

def wing( angle=0 ):
    wing_rim_wood_thickness = .75
    return [
        #Attachment
        translate( [0, 0, -3.5 - .5] ) (
            pins( 3.5+1.5 )
        ),
        translate( [-5.5 + 3, 0, -.5] ) (
            cube_rot( [1, 2, 0] ) (
                wood_2x6( cart_depth )
            )
        ),
        translate( [1.5, 0, -3.5 - .5] ) (
            cube_rot( [0, 2, 1] ) (
                wood_2x4( cart_depth )
            ) - translate( [-1.5, 0, 0] ) ( pins( 3.5+1.5 ) )
        ),
        #Moving part
        translate( [3, 0, 0] ) (
            rotate( v=[0,1,0], a=angle ) (
                wood( [wing_width, wing_rim_wood_thickness, wing_height] ),
                translate( [0, cart_depth-wing_rim_wood_thickness, 0] ) (
                    wood( [wing_width, wing_rim_wood_thickness, wing_height] )
                ),
                translate( [0, wing_rim_wood_thickness, 0] ) (
                    wood( [wing_rim_wood_thickness, cart_depth-wing_rim_wood_thickness*2, wing_height] )
                ),
                translate( [wing_width-wing_rim_wood_thickness, wing_rim_wood_thickness, 0] ) (
                    wood( [wing_rim_wood_thickness, cart_depth-wing_rim_wood_thickness*2, wing_height] )
                ),
                translate( [0, 0, wing_height] ) (
                    plywood( wing_width, cart_depth )
                )
            )
        )
    ]

parts.append(
    translate( [1.5 * 2, 1.5*2, shelf_height_above_ground] ) (
        bottom_shelf()
    )
)

parts += [
    translate( [1.5, 1.5, shelf_height_above_ground] ) (
        leg()
    ),
    translate( [cart_width-1.5, 1.5, shelf_height_above_ground] ) (
        scale( [-1, 1, 1] ) (
            leg()
        )
    ),
    translate( [cart_width-1.5, cart_depth-1.5, shelf_height_above_ground] ) (
        scale( [-1, -1, 1] ) (
            leg()
        )
    ),
    translate( [1.5, cart_depth-1.5, shelf_height_above_ground] ) (
        scale( [1, -1, 1] ) (
            leg()
        )
    )
]

parts += [
    translate( [0, 0, cart_height-3.5 - .5] ) (
        rim()
    )
]

parts += [
    translate( [5.5-1.5, 0, cart_height-.5] ) (
        plywood( platform_width, cart_depth )
    )
]


wings = [
    translate( [cart_width-1.5, 0, cart_height] ) (
        wing()
    ),
    translate( [1.5, 0, cart_height] ) (
        scale( [-1, 1, 1] ) (
            wing()
        )
    )
]

if wing_lifted:
    wings = up( 6 ) (
        wings
    )

parts += [wings]


print( wood_bom() )

#ALl dimensions above are in inches
parts = scale( mm_to_in ) ( parts )

print( "Saving File" )
with open( __file__ + ".scad", "w" ) as f:
    f.write( scad_render( union() ( parts ) ) )
