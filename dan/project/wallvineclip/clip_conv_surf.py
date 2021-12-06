import math
import random
import functools
from dataclasses import dataclass

from solid import *
from solid.utils import *

from lib.helper import *
from lib import pyconvsurf

parts = []

base_size = 20
base_height = 5
hook_radius = 15
hook_thickness = 7
screw_head_top_rad = 4
screw_bottom_rad = 2
screw_cone_height = 3.5


def basic_shape():
    surf = pyconvsurf.ConvSurf(margin=15, resolution=0.5)

    # Add base
    base_s = 2.2
    corner_distance = base_size * 0.5 - 3
    corners = [
        [-corner_distance, -corner_distance, 0],
        [corner_distance, -corner_distance, 0],
        [corner_distance, corner_distance, 0],
        [-corner_distance, corner_distance, 0],
    ]
    surf.add_triangle(corners[0], corners[1], corners[2], s=base_s)
    surf.add_triangle(corners[0], corners[2], corners[3], s=base_s)

    # Add hooks
    angle = 165
    angle_rads = math.radians(angle)
    num_points = 13
    angle_per_point = angle_rads / num_points
    total_distance = angle_rads * hook_radius
    curved_tip_start = math.ceil(
        num_points - (hook_thickness / total_distance) * num_points
    )
    angles = [angle_per_point * i for i in range(num_points)]

    points = [
        Vec3(
            math.sin(a) * hook_radius,
            a * 0.001,
            hook_radius - math.cos(a) * hook_radius,
        )
        for a in angles
    ]

    # points = points[5:]

    hook_s = 1.5
    for a, b in pairwise(points):
        surf.add_line(
            a.to_list(),
            b.to_list(),
            s=hook_s,
        )
        surf.add_line(
            (a * Vec3(-1, 1, 1)).to_list(),
            (b * Vec3(-1, 1, 1)).to_list(),
            s=hook_s,
        )

    # import random

    # for i in range(5):
    #     surf.add_triangle(
    #         [random.uniform(0, 40), random.uniform(0, 40), random.uniform(0, 40)],
    #         [random.uniform(0, 40), random.uniform(0, 40), random.uniform(0, 40)],
    #         [random.uniform(0, 40), random.uniform(0, 40), random.uniform(0, 40)],
    #         s=3,
    #     )
    #     # surf.add_line(
    #     #     [random.uniform(10, 50), random.uniform(10, 50), random.uniform(10, 50)],
    #     #     [random.uniform(10, 50), random.uniform(10, 50), random.uniform(10, 50)],
    #     #     s=2,
    #     # )
    #     surf.add_line(
    #         [0, 0, 0],
    #         [0, 0, 50],
    #         s=1,
    #     )

    # Something is wrong with the auto field setting, causing all kinds of crazy results
    surf.minx = -30.0
    surf.miny = -30.0
    surf.minz = -10.0
    surf.maxx = 30.0
    surf.maxy = 30.0
    surf.maxz = 50.0
    vertices, triangles = surf.generate(isovalue=0.005)
    print(f"num vertices: {len(vertices)}")
    return polyhedron(points=vertices, faces=triangles)


def screw_hole():
    segments = 24
    return hole()(
        down(1)(cylinder(r=screw_bottom_rad, h=base_height + 2, segments=segments)),
        up(base_height - screw_cone_height)(
            cylinder(
                r1=screw_bottom_rad,
                r2=screw_head_top_rad,
                h=screw_cone_height + 0.001,
                segments=segments,
            )
        ),
        up(base_height)(cylinder(r=screw_head_top_rad, h=10, segments=segments)),
    )


bottom_remove = hole()(
    translate([-base_size, -base_size, -base_size])(
        cube([base_size * 2, base_size * 2, base_size])
    )
)

parts += [basic_shape(), screw_hole(), bottom_remove]

print("Saving File")
with open(__file__ + ".scad", "w") as f:
    f.write(scad_render(union()(parts)))