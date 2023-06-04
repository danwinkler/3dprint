import math
import random
from dataclasses import dataclass

import numpy as np
from lib.helper import *
from solid import *
from solid.utils import *

parts = []

radius = 100
slot_width = 5  # arm is 4 wide

a = 10
b = 0.035
c = math.pi * 0.5
d = 13

x = np.linspace(0, radius, 40)
y = a * np.sin(b * x + c) + d

points = [(_x, _y) for _x, _y in zip(x, y)]

points += [(radius, 0), (0, 0)]

cross_section = polygon(points=points)

base = rotate_extrude(angle=360, segments=60)(cross_section)

cutout = translate([0, 0, -0.01])(
    scale(1.2)(
        rotate(a=10, v=[0, 0, 1])(rotate_extrude(angle=100, segments=60)(cross_section))
    )
) - cylinder(r=20, h=50)

for angle in np.linspace(0, 360, 4):
    base -= rotate(a=angle, v=[0, 0, 1])(cutout)

base_with_slots = base.copy()

slots = []
for angle in np.linspace(0, 360, 4):
    slots += [
        rotate(a=angle, v=[0, 0, 1])(
            translate([0, -slot_width / 2, 0])(cube([radius - 5, slot_width, 100]))
        )
    ]

parts += up(3)([base_with_slots - union()(slots)])

parts += [base]

print("Saving File")
with open(__file__ + ".scad", "w") as f:
    f.write(scad_render(union()(parts)))
