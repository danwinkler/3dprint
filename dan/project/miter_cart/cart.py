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
cart_width = 26
cart_depth = 24
cart_height = 36
shelf_height_above_ground = 4
wing_height = 5
wing_width = 24

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
    leg_board_length = cart_height - shelf_height_above_ground
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

def rim():
    return [
        wood_2x4( cart_width ),
        translate( [0, cart_depth-1.5, 0] ) (
            wood_2x4( cart_width )
        ),
        translate( [0, 1.5, 0] ) (
            cube_rot( [0, 2, 1] ) (
                wood_2x4( cart_depth - 1.5*2 )
            )
        ),
        translate( [cart_width-1.5, 1.5, 0] ) (
            cube_rot( [0, 2, 1] ) (
                wood_2x4( cart_depth - 1.5*2 )
            )
        )
    ]

def wing( angle=0 ):
    wing_rim_wood_thickness = .75
    return rotate( v=[0,1,0], a=angle ) (
        wood( [wing_width, wing_rim_wood_thickness, wing_height-.5] ),
        translate( [0, cart_depth-wing_rim_wood_thickness, 0] ) (
            wood( [wing_width, wing_rim_wood_thickness, wing_height-.5] )
        ),
        translate( [0, wing_rim_wood_thickness, 0] ) (
            wood( [wing_rim_wood_thickness, cart_depth-wing_rim_wood_thickness*2, wing_height-.5] )
        ),
        translate( [wing_width-wing_rim_wood_thickness, wing_rim_wood_thickness, 0] ) (
            wood( [wing_rim_wood_thickness, cart_depth-wing_rim_wood_thickness*2, wing_height-.5] )
        ),
        translate( [0, 0, wing_height-.5] ) (
            plywood( wing_width, cart_depth )
        )
    )

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
    translate( [0, 0, cart_height-3.5] ) (
        rim()
    )
]

parts += [
    translate( [0, 0, cart_height] ) (
        plywood( cart_width, cart_depth )
    )
]

parts += [
    translate( [cart_width, 0, cart_height+.5] ) (
        wing()
    ),
    translate( [0, 0, cart_height+.5] ) (
        scale( [-1, 1, 1] ) (
            wing()
        )
    )
]



print( wood_bom() )

#ALl dimensions above are in inches
parts = scale( mm_to_in ) ( parts )

print( "Saving File" )
with open( __file__ + ".scad", "w" ) as f:
    f.write( scad_render( union() ( parts ) ) )
