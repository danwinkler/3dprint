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
    points = [ Vec3(0,0,0) ]
    points += [ Vec3( r+r*cos(t), r*sin(t)+base_h, 0 ) for t in np.linspace(math.pi,math.pi/2,steps) ]

    arch = vine( points, lambda h,a: thick, sections=16 )

    # SHAVE the top to make the two half arches join nicely
    arch -= translate([w,0,-thick*2])( cube([r*2,base_h+2*r,thick*4]) )

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
        gothic_arch( 0.50*face_h,     w, w*2.9, 5 ) +
        gothic_arch( 0.48*face_h, 0.8*w, w*2.8, 3 )
    )

    gt = gothic_triangle(10,0.5,1,20);
    inner_r = 4.6
    cutout_r = 4.6
    for i in range(3):
        a = i * math.pi*2 / 3
        gt -= translate([inner_r*math.cos(a),inner_r*math.sin(a),-1])( cylinder(r=cutout_r,h=3,segments=25) )


    decor += translate([0,0,10])(
        rotate(360/6,[0,0,1])(
            gt
        )
    )
    

    # SHAVE back
    decor -= translate([0,0,-100]) (
        cube([face_w,face_h*2,100])
    )

    return decor

def gothic_triangle(r,r_percent,thick,segments):
    pts = []
    trifold_angles = [ 0*math.pi*2/3, 1*math.pi*2/3, 2*math.pi*2/3 ]
    trifold_vecs = [ Vec3(r*math.cos(a),r*math.sin(a),0) for a in trifold_angles ]
    for i in range(3):
        p = trifold_vecs[(0+i)%3] * r_percent
        q1 = trifold_vecs[(1+i)%3] - p
        a1 = math.atan2(q1.y,q1.x)
        while a1 < 0:
            a1 += math.pi*2
        q2 = trifold_vecs[(2+i)%3] - p
        a2 = math.atan2(q2.y,q2.x)
        while a2 < 0 or a2 < a1:
            a2 += math.pi*2
        r = q1.length()
        pts += [ [r*math.cos(a)+p.x,r*math.sin(a)+p.y] for a in np.linspace(a1,a2,segments) ]

    return linear_extrude( thick, True, 1, 0, 1, 1 )(
        polygon( points=pts )
    )

face = (face_base() + decoration())
# face = (face_base() + decoration()) - rim()

# REMOVE the switch
# face -= translate( [(face_w-10.4)/2, (face_h-24.5)/2, -1] ) (
#     cube( [10.4, 24.5, 100] )
# )

# def screw_hole():
#     return translate( [face_w/2, 0, -.001] ) (
#         cylinder( r1=4.6/2, r2=7.5/2, h=2.002, segments=16 ) +
#         up( 2 ) ( cylinder( r=7.5/2, h=100 ) )
#     )

# face -= translate( [0, +22.7, 0] ) ( screw_hole() )
# face -= translate( [0, face_h-22.7, 0] ) ( screw_hole() )

if __name__ == '__main__':
    print "Saving File"

    with open( __file__ + "_rim.scad", "w" ) as f:
        f.write( scad_render( rim()) )

    with open( __file__ + "_face.scad", "w" ) as f:
        f.write( scad_render( union() ( face ) ) )
