import copy
import math
import random
import platform
import os
from pathlib import Path

from solid import *
from solid.utils import *
from tqdm import tqdm
from plumbum import local
import pyclipper

from dan.lib.helper import *
from dan.lib import polytri
from dan.project.slicestack.differential_line import DiffLine, NodeData

df = DiffLine()
df.init_circle()

layers = []
height = 160
flip = False

for i in tqdm(range(height)):
    df.update()

    if i % 10 == 0:
        layer = []
        for n in df.nodes:
            nd = NodeData(n)
            if flip:
                nd.pos.z = height - i
            else:
                nd.pos.z = i
            layer.append(nd.pos)
        layers.append(layer)

parts = []


def shrink_layer(layer, offset):
    z = layer[0].z

    pco = pyclipper.PyclipperOffset()
    pco.AddPath(
        [(p.x, p.y) for p in layer],
        pyclipper.JT_ROUND,
        pyclipper.ET_CLOSEDPOLYGON
    )

    solution = pco.Execute(-offset)

    if len(solution) > 1:
        print( "warning, solution len: {}".format(len(solution)))

    # Only use the longest solution, if there's more than one we're probably fucked anyhow
    path = max(solution, key=lambda d: len(d))

    return [Vec3(p[0], p[1], z) for p in path]


shrink_amount = 5
shrunk_layers = [shrink_layer(layer, shrink_amount) for layer in layers]

outer = rings_to_polyhedron(layers[:-1], progress_stdout=True)
inner = rings_to_polyhedron(shrunk_layers[1:], progress_stdout=True)

#parts.append( outer )
#parts.append( inner )
parts.append(outer - inner)

print("Saving File")
with open(__file__ + ".scad", "w") as f:
    f.write(scad_render(union()(parts)))
