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
height = 100
flip = False

for i in tqdm(range(height)):
    df.update()

    if i % 5 == 0:
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
        [(p.x, p.y) for p in layer], pyclipper.JT_SQUARE, pyclipper.ET_CLOSEDPOLYGON
    )

    solution = pco.Execute(-offset)

    # Only use the first solution, if there's more than one we're fucked anyhow
    return [Vec3(p[0], p[1], z) for s in solution[0]]


shrink_amount = 2
shrunk_layers = [shrink_layer(layer, shrink_amount) for layer in layers]

outer = rings_to_polyhedron(layers[:-1])
inner = rings_to_polyhedron(shrunk_layers[1:])

# parts.append( outer )
parts.append(outer - inner)

print("Saving File")
with open(__file__ + ".scad", "w") as f:
    f.write(scad_render(union()(parts)))
