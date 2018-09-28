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
    up = Vec3(0, 0, 1)
    new_layer = []
    for i, p in enumerate(layer):
        n = layer[(i+1) % len(layer)]

        v = n - p
        c = v.cross(up)
        c.normalize()
        c *= -offset
        new_pos = n + c
        new_layer.append(new_pos)
    return new_layer

shrink_amount = 2
shrunk_layers = [shrink_layer(layer, shrink_amount) for layer in layers]

outer = rings_to_polyhedron(layers[:-1])
inner = rings_to_polyhedron(shrunk_layers[1:])

# parts.append( outer )
parts.append( outer - inner )

"""

folder =  Path( os.path.dirname(os.path.realpath(__file__)) )
file_a = folder / 'outer.scad'
file_b = folder / 'inner.scad'
stl_a = folder / 'a.stl'
stl_b = folder / 'b.stl'

with open(file_a, 'w') as f:
    f.write(scad_render(union()(outer)))

with open(file_b, 'w') as f:
    f.write(scad_render(union()(inner)))

system = platform.system()
if system == "Windows":
    pgm = "C:\Program Files\OpenSCAD\openscad.exe"
else:
    pgm = "/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD"

openscad = local[pgm]

print('Building a')
openscad('-o', stl_a, file_a)

print('Building b')
openscad('-o', stl_b, file_b)

parts = import_stl(str(stl_a).replace('\\', '/')) - import_stl(str(stl_b).replace('\\', '/'))
"""

print( "Saving File" )
with open( __file__ + ".scad", "w" ) as f:
    f.write( scad_render( union() ( parts ) ) )

