import math
import random
from dataclasses import dataclass

from lib.helper import *
from solid import *
from solid.utils import *

parts = []

servo_width = 23 + 0.5
servo_length = 12 + 0.5

base_thickness = 3

hole_dist_from_servo_body = 2.65
arm_width = hole_dist_from_servo_body * 2


def servo_mount():
    def mount_arm():
        height = servo_length
        arm_thickness = 5
        arm = cube([arm_width, arm_thickness, base_thickness + height])

        arm_hole = translate(
            [hole_dist_from_servo_body, 0, base_thickness + (servo_length / 2)]
        )(
            rotate(a=-90, v=[1, 0, 0])(
                down(0.5)(cylinder(r=1.5, h=arm_thickness + 1, segments=16))
            )
        )

        return arm - arm_hole

    arm_a = mount_arm()

    arm_b = translate([servo_width + arm_width, 0, 0])(mount_arm())

    return arm_a + arm_b


def base(n_servos=3, servo_distance=50):
    arm_width = 15

    servo_offset = 12

    arms = []
    for i in range(n_servos):
        angle = i * (360 / n_servos)

        neg_x_dist = 0
        arms += [
            rotate(a=angle, v=[0, 0, 1])(
                translate([-neg_x_dist, -arm_width / 2 + servo_offset, 0])(
                    cube(
                        [
                            neg_x_dist + servo_distance + (servo_width + arm_width) / 2,
                            arm_width,
                            base_thickness,
                        ]
                    )
                )
                + translate(
                    [servo_distance - (servo_width + arm_width) / 2, servo_offset, 0]
                )(servo_mount())
            )
        ]

    center_cyl_rad = arm_width / 2
    center_cyl_height = 10
    center_cyl = cylinder(r=center_cyl_rad, h=center_cyl_height, segments=32)
    center_cyl -= translate([0, 0, center_cyl_height])(
        sphere(r=center_cyl_rad - 1, segments=32)
    )

    center_cyl += cylinder(
        r=arm_width / 2 + servo_offset, h=base_thickness, segments=64
    )

    return union()(arms, center_cyl)


parts.append(base(n_servos=4, servo_distance=50))


print("Saving File")
with open(__file__ + ".scad", "w") as f:
    f.write(scad_render(union()(parts)))
