import math
import pathlib
import random
from dataclasses import dataclass

from lib.helper import *
from solid import *
from solid.utils import *

parts = []

arm_length = 100
arm_width = 10
arm_thickness = 4
arm_round = 1.9


def round_cube(size, r):
    shrunk_size = [s - r * 2 for s in size]
    return translate([r, r, r])(minkowski()(cube(shrunk_size), sphere(r, segments=16)))


def triangle_arm():
    radius = arm_thickness * 0.5
    return hull()(
        translate([radius, radius, radius])(sphere(r=radius, segments=16)),
        translate([radius, arm_width - radius, radius])(sphere(r=radius, segments=16)),
        translate([arm_length - radius, arm_width * 0.5, radius])(
            sphere(r=radius, segments=16)
        ),
    )


def arm():
    # body = round_cube([arm_length, arm_width, arm_thickness], arm_round)
    body = triangle_arm()

    # For some reason this stl isn't centered on the origin, so we need to shift it
    model_offset = [85, -110, 0]
    servo_mounted_arm = translate(model_offset)(
        import_stl(pathlib.Path(__file__).parent / "Servo_Arm.stl")
    )

    arm_extra_amount = 0.2

    body -= up(1)(
        union()(
            servo_mounted_arm,
            # subtract arm a bit to side to side and up and down to make it fit
            translate([0, arm_extra_amount, 0])(servo_mounted_arm),
            translate([0, -arm_extra_amount, 0])(servo_mounted_arm),
            translate([0, 0, arm_extra_amount])(servo_mounted_arm),
            translate([0, 0, -arm_extra_amount])(servo_mounted_arm),
            # To erase the holes, offset it a bit and subtract again
            translate([-1, 0, -arm_extra_amount])(servo_mounted_arm),
            translate([-1, 0, arm_extra_amount])(servo_mounted_arm),
            # Get rid of the screw hole in th negative space
            translate([0, 5, 0])(cylinder(r=3, h=4)),
        )
    )

    # add the screw hole for the hole heigh
    body -= translate([0, 5, -0.1])(cylinder(r=2, h=4, segments=16))

    return body


parts.append(arm())

print("Saving File")
with open(__file__ + ".scad", "w") as f:
    f.write(scad_render(union()(parts)))
