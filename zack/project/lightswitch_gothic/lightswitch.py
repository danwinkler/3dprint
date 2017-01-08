import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

import numpy as np


face_w = 70
face_h = 115
face_d = 2

def rim():
    lip_rad = 5
    solid_rim = minkowski() (
        cube( [face_w, face_h, .0001] ),
        sphere( r=lip_rad, segments=24 ) - (
            translate( [-lip_rad,-lip_rad,-lip_rad] ) (
                cube([10,10,5] )
            )
        )
    )

    inset = 3
    tolerance = 0.2

    # Z position so that the face is sitting at zero and the rim is slightly
    # down. This allows you to subtract off the rim from the decorations
    return translate([0,0,-lip_rad+face_d])(
        solid_rim - (
            # REMOVE all the way through
            translate( [inset/2, inset/2, -1] ) (
                cube( [face_w-inset, face_h-inset, lip_rad+2] )
            )
            +
            # REMOVE space for the face plate
            translate( [-tolerance, -tolerance, lip_rad-face_d-tolerance] ) (
               cube( [face_w+2*tolerance, face_h+2*tolerance, lip_rad+2] )
            )
        )
    )

def half_arch(base_h,w,r,thick):
    def arc(r,x):
        return math.sqrt(r**2-(r-x)**2)+base_h

    steps = 10
    x_step = w / steps
    points = [ Vec3(0,0,0) ]

    # Have dense steps for the first bit
    points += [ Vec3( x, arc(r,x), 0 ) for x in np.linspace(0,x_step,steps/2) ]

    # Then not as dense steps
    points += [ Vec3( x, arc(r,x), 0 ) for x in np.linspace(2*x_step,w*1.1,steps) ]

    arch = vine( points, lambda h,a: thick, sections=16 )

    # SHAVE the top to make the two half arches join nicely
    arch -= translate([w,0,-thick*2])( cube([thick*4,base_h+r,thick*4]) )

    return arch

def gothic_arch(base_h,w,r,thick):
    def ha():
        return half_arch(base_h,w,r,thick)

    return union()(
        translate([0,0,0])(
            translate([-w,0,0])(
                mirror([0,0,0])(
                    ha()
                )
            ),
            translate([w,0,0])(
                mirror([1,0,0])(
                    ha()
                )
            ),
        ),
    )

def face_base():
    return cube([face_w,face_h,face_d])

def decoration():
    w = face_w / 2.5
    decor = translate([face_w/2,0,3])(
        gothic_arch( 0.50*face_h,     w, face_w*1.5, 5 ) +
        gothic_arch( 0.48*face_h, 0.8*w, face_w*1.5, 3 )
    )

    # SHAVE back
    decor -= translate([0,0,-100]) (
        cube([face_w,face_h*2,100])
    )

    return decor


face = (face_base() + decoration()) - rim()

# REMOVE the switch
face -= translate( [(face_w-10.4)/2, (face_h-24.5)/2, -1] ) (
    cube( [10.4, 24.5, 100] )
)

def screw_hole():
    return translate( [face_w/2, 0, -.001] ) (
        cylinder( r1=4.6/2, r2=7.5/2, h=2.002, segments=16 ) +
        up( 2 ) ( cylinder( r=7.5/2, h=100 ) )
    )

face -= translate( [0, +22.7, 0] ) ( screw_hole() )
face -= translate( [0, face_h-22.7, 0] ) ( screw_hole() )

if __name__ == '__main__':
    print "Saving File"

    with open( __file__ + "_rim.scad", "w" ) as f:
        f.write( scad_render( rim()) )

    with open( __file__ + "_face.scad", "w" ) as f:
        f.write( scad_render( union() ( face ) ) )
