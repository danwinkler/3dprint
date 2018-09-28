from dan.lib import glfw
from dan.project.slicestack.differential_line import DiffLine

from p5 import *

dl = DiffLine()


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

    for i, node in enumerate(nodes):
        next = nodes[(i + 1) % len(nodes)]
        line((node.pos.x, node.pos.y), (next.pos.x, next.pos.y))
        # circle((node.pos.x, node.pos.y), 4)

    reset_matrix()


run()
