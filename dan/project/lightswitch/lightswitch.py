import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

x = 115
y = 70
z = 5

parts = []

solid_rim = translate( [5, 5, 0] ) (
    minkowski() (
        cube( [115 - 10, 70 - 10, .0001] ),
        sphere( r=5, segments=24 ) - translate( [-5,-5,-5] ) ( cube([10,10,5] ) )
    )
)

rim = solid_rim - (
    translate( [5, 5, -1] ) (
        cube( [x - 10, y - 10, 10] )
    ) +
    translate( [4, 4, 3] ) (
        cube( [x - 8, y - 8, 10] )
    )
)

fx = x - 8 - .1
fy = y - 8 - .1

face = cube( [fx, fy, 2] ) + hole()(
    translate( [(fx-24.5)/2, (fy-10.4)/2, -1] ) (
        cube( [24.5, 10.4, 1000] )
    ) +
    translate( [22.7,fy/2,-.001] ) (
        cylinder( r1=4.6/2, r2=7.5/2, h=2.002, segments=16 ) +
        up( 2 ) ( cylinder( r=7.5/2, h=1000 ) )
    )
    +
    translate( [fx-22.7,fy/2,-.001] ) (
        up( 2 ) ( cylinder( r=7.5/2, h=1000 ) ) +
        cylinder( r1=4.6/2, r2=7.5/2, h=2.002, segments=16 )
    )
)

face += hole() (
    translate( [-1000, -1000, -100] ) (
        cube( [2000, 2000, 100] )
    ) +
    translate( [-1000, -1000, 0 ] ) (
        cube( [1000, 2000, 2] )
    ) +
    translate( [fx, -1000, 0 ] ) (
        cube( [1000, 2000, 2] )
    ) +
    translate( [0, fy, 0 ] ) (
        cube( [1000, 1000, 2] )
    ) +
    translate( [0, -1000, 0] ) (
        cube( [1000, 1000, 2] )
    )
)

if __name__ == '__main__':
    print "Saving File"
    with open( __file__ + "_rim.scad", "w" ) as f:
        f.write( scad_render( union() ( rim ) ) )

    with open( __file__ + "_face.scad", "w" ) as f:
        f.write( scad_render( union() ( face ) ) )
