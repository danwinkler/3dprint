import math
import random
import functools
from dataclasses import dataclass

from solid import *
from solid.utils import *

from lib.helper import *

parts = []

base_size = 20
base_height = 5
hook_radius = 15
hook_thickness = 7
screw_head_top_rad = 4
screw_bottom_rad = 2
screw_cone_height = 3.5


def base():
    segments = 24
    corner_distance = base_size * 0.5 - base_height
    corners = [
        translate([-corner_distance, -corner_distance, 0])(
            sphere(r=base_height, segments=segments)
        ),
        translate([corner_distance, -corner_distance, 0])(
            sphere(r=base_height, segments=segments)
        ),
        translate([corner_distance, corner_distance, 0])(
            sphere(r=base_height, segments=segments)
        ),
        translate([-corner_distance, corner_distance, 0])(
            sphere(r=base_height, segments=segments)
        ),
    ]

    return hull()(corners)


def hook():
    segments = 24
    angle = 280

    def cap(a):
        return rotate(a, [0, 0, 1])(
            translate([hook_radius, 0, 0])(
                rotate(90, [1, 0, 0])(sphere(r=hook_thickness * 0.5, segments=segments))
            )
        )

    rot_angle = angle + 90 + (360 - angle) * 0.5
    ring_shape = rotate(a=-rot_angle, v=[0, 0, 1])(
        rotate_extrude(angle=angle, segments=segments * 2)(
            translate([-hook_radius, 0])(
                circle(r=hook_thickness * 0.5, segments=segments)
            )
        )
        + cap(angle + 180)
        + cap(180)
    )

    ring = translate([0, 0, hook_radius])(rotate(90, [1, 0, 0])(ring_shape))

    return ring


def screw_hole():
    segments = 24
    return hole()(
        down(1)(cylinder(r=screw_bottom_rad, h=base_height + 2, segments=segments)),
        up(base_height - screw_cone_height)(
            cylinder(
                r1=screw_bottom_rad,
                r2=screw_head_top_rad,
                h=screw_cone_height,
                segments=segments,
            )
        ),
    )


bottom_remove = hole()(
    translate([-base_size, -base_size, -base_height])(
        cube([base_size * 2, base_size * 2, base_height])
    )
)

parts += [base(), hook(), screw_hole(), bottom_remove]

print("Saving File")
with open(__file__ + ".scad", "w") as f:
    f.write(scad_render(union()(parts)))
