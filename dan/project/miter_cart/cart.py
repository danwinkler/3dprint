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
cart_width = platform_width + 1.5*2
cart_depth = 24
cart_height = 36
shelf_height_above_ground = 4
wing_height = 5
wing_width = 24
wing_tongue_length = 18
wing_tongue_thickness = .75

wing_lifted = False

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

def rim():
    wing_slot_thickness = wing_tongue_thickness
    return [
        translate( [-wing_slot_thickness, 0, 0] ) (
            wood_2x4( cart_width + wing_slot_thickness*2 )
        ),
        translate( [-wing_slot_thickness, cart_depth-1.5, 0] ) (
            wood_2x4( cart_width + wing_slot_thickness*2 )
        ),
        #Left
        translate( [-wing_slot_thickness, 1.5, 0 ] ) (
            cube_rot( [0, 2, 1] ) (
                wood_2x4( cart_depth - 1.5*2 )
            )
        ),
        #Right
        translate( [cart_width + wing_slot_thickness - 1.5, 1.5, 0] ) (
            cube_rot( [0, 2, 1] ) (
                wood_2x4( cart_depth - 1.5*2 )
            )
        )
    ]

def wing( angle=0 ):
    wing_rim_wood_thickness = .75
    wing_lower_height = 0
    return [
        #Attachment
        translate( [0, 1.5, -wing_tongue_length + 3.5 - .5] ) (
            cube_rot( [0, 2, 1] ) (
                plywood( cart_depth - 1.5*2, wing_tongue_length, wing_tongue_thickness )
            )
        ),
        translate( [wing_tongue_thickness, 0, -.5] ) (
            cube_rot( [0, 2, 1] ) (
                wood_2x4( cart_depth )
            )
        ),
        #Moving part
        translate( [1.5 + wing_tongue_thickness, 0, 0] ) (
            rotate( v=[0,1,0], a=angle ) (
                translate( [0, 0, -wing_lower_height] ) (
                    wood( [wing_width, wing_rim_wood_thickness, wing_height+wing_lower_height] )
                ),
                translate( [0, cart_depth-wing_rim_wood_thickness, -wing_lower_height] ) (
                    wood( [wing_width, wing_rim_wood_thickness, wing_height+wing_lower_height] )
                ),
                translate( [0, wing_rim_wood_thickness, -wing_lower_height] ) (
                    wood( [wing_rim_wood_thickness, cart_depth-wing_rim_wood_thickness*2, wing_height+wing_lower_height] )
                ),
                translate( [wing_width-wing_rim_wood_thickness, wing_rim_wood_thickness, -wing_lower_height] ) (
                    wood( [wing_rim_wood_thickness, cart_depth-wing_rim_wood_thickness*2, wing_height+wing_lower_height] )
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
    translate( [(cart_width-platform_width) * .5, 0, cart_height-.5] ) (
        plywood( platform_width, cart_depth )
    )
]

parts += [
    translate( [0, 1.5, cart_height - wing_tongue_length - 1.5 + 1] ) (
        cube_rot( [0, 2, 1] ) (
            wood_2x4( cart_depth-3 )
        )
    ),
    translate( [cart_width - 1.5, 1.5, cart_height - wing_tongue_length - 1.5 + 1] ) (
        cube_rot( [0, 2, 1] ) (
            wood_2x4( cart_depth-3 )
        )
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
    wings = up( wing_tongue_length + 3 ) (
        wings
    )

parts += [wings]


print( wood_bom() )

for i in range( 10 ):
    plywood( 10, 20 )

pack2x4 = wood_pack_1d( '2x4', length=8*12 )
pack2x6 = wood_pack_1d( '2x6', length=8*12 )

pack_plywood5 = wood_pack_2d( 'plywood-0.5', width=4*12, length=8*12 )
pack_plywood75 = wood_pack_2d( 'plywood-0.75', width=4*12, length=8*12 )

print( "Pack 2x4 - " + str(len(pack2x4)) )
print( pack2x4 )

print( "Pack 2x6 - " + str(len(pack2x6)) )
print( pack2x6 )

print( "Pack plywood .5 - " + str(len(pack_plywood5)) )
#print( pack_plywood5 )

print( "Pack plywood .75 - " + str(len(pack_plywood75)) )
#print( pack_plywood75 )

#ALl dimensions above are in inches
parts = scale( mm_to_in ) ( parts )

print( "Saving File" )
with open( __file__ + ".scad", "w" ) as f:
    f.write( scad_render( union() ( parts ) ) )
