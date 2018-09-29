import pyclipper

from dan.lib import glfw
from dan.lib.helper import Vec3
from dan.project.slicestack.differential_line import DiffLine

from p5 import *


dl = DiffLine()

def shrink_layer(layer, offset):
    z = layer[0].z

    pco = pyclipper.PyclipperOffset()
    pco.AddPath(
        [(p.x, p.y) for p in layer],
        pyclipper.JT_SQUARE,
        pyclipper.ET_CLOSEDPOLYGON
    )

    solution = pco.Execute(-offset)

    if len(solution) > 1:
        print( "warning, solution len: {}".format(len(solution)))

    # Only use the longest solution, if there's more than one we're probably fucked anyhow
    path = max(solution, key=lambda d: len(d))

    return [Vec3(p[0], p[1], z) for p in path]

def setup():
    size(800, 600)
    # no_stroke()
    stroke(0)
    dl.init_circle()


def draw():
    dl.update()

    background(255)

    push_matrix()
    translate(width * 0.5, height * 0.5)

    nodes = dl.get_nodes()

    points = [n.pos for n in nodes]

    shrunk_points = shrink_layer(points, 2)

    for i, p in enumerate(points):
        next = points[(i + 1) % len(points)]
        line((p.x, p.y), (next.x, next.y))
    
    for i, p in enumerate(shrunk_points):
        next = shrunk_points[(i + 1) % len(shrunk_points)]
        line((p.x, p.y), (next.x, next.y))

    reset_matrix()


run()
