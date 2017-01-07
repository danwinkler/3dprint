import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

import numpy as np

x = 115
y = 70
z = 5

solid_rim = minkowski() (
    cube( [115, 70, .0001] ),
    sphere( r=5, segments=24 ) - translate( [-5,-5,-5] ) ( cube([10,10,5] ) )
)

rim = solid_rim - (
    translate( [1, 1, -1] ) (
        cube( [x-2, y-2, 10] )
    ) +
    translate( [-.2, -.2, 3] ) (
        cube( [x+.4, y+.4, 10] )
    )
)

fx = x
fy = y

def half_arch():
    r = 1.5
    points = [ Vec3( x, math.sqrt(r**2-(r-x)**2), 0 ) for x in np.linspace(0,0.6,20) ]
    arch = vine( points, lambda h,a: 0.05, sections=16 )
    arch = difference()(
        arch,
        translate([0.5,0,-0.5])(
            cube([1,5,1])
        )
    )
    arch = union() (
        arch,
        translate([0,0.02,0])(
            rotate(90,[1,0,0])(
                cylinder(0.05,1.2,segments=16)
            )
        )
    )
    return arch

def gothic_arch():
    return union()(
        translate([0,1.2,0])(
            translate([-0.5,0,0])(
                mirror([0,0,0])(
                    half_arch()
                )
            ),
            translate([0.5,0,0])(
                mirror([1,0,0])(
                    half_arch()
                )
            ),
        ),
    )

def gothic_arch_scaled_for_switch():
    return translate([115,35,0]) (
        scale([60,60,60])(
            rotate(90,[0,0,1])(
                gothic_arch()
            )
        )
    )

decoration = cube( [fx, fy, 2] )
decoration += gothic_arch_scaled_for_switch()

face = difference()(
    decoration,
    translate( [(fx-24.5)/2, (fy-10.4)/2, -1] ) (
        cube( [24.5, 10.4, 1000] )
    )
)

face = difference()(
    face,
    translate([0,0,-3])(
        rim
    )
)

if __name__ == '__main__':
    print "Saving File"
    with open( __file__ + "_rim.scad", "w" ) as f:
        f.write( scad_render( union() ( rim ) ) )

    with open( __file__ + "_face.scad", "w" ) as f:
        f.write( scad_render( union() ( face ) ) )
