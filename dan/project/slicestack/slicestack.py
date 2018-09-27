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
height = 200
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
            layer.append(nd)
        layers.append(layer)

parts = []

def shrink_layer(layer, offset):
    up = Vec3(0, 0, 1)
    new_layer = []
    for i, p in enumerate(layer):
        n = layer[(i+1) % len(layer)]

        v = n.pos - p.pos
        c = v.cross(up)
        c.normalize()
        c *= -offset
        new_pos = n.pos + c
        ncopy = copy.deepcopy(n)
        ncopy.pos = new_pos
        new_layer.append(ncopy)
    return new_layer

shrink_amount = 2
shrunk_layers = [shrink_layer(layer, shrink_amount) for layer in layers]

def set_closest_for_layer(nd, layer):
    min_dist = 100000000
    min_point = None
    for o in layer:
        d2 = o.pos.distance2(nd.pos)
        if d2 < min_dist:
            min_point = o
            min_dist = d2
    nd.opposite = min_point

def build_object(layers):
    pb = PolyhedronBuilder()

    def build_layers(pb, layers):
        for z, layer in tqdm(enumerate(layers), total=len(layers)):
            if z+1 == len(layers):
                break

            next_layer = layers[z+1]

            ai = 0
            bi = 0
            while bi < len(next_layer):
                b0 = next_layer[bi]
                b1 = next_layer[(bi+1) % len(next_layer)]
                a0 = layer[ai%len(layer)]
                a1 = layer[(ai+1)%len(layer)]

                pb.triangle(b0.pos, a0.pos, b1.pos)

                bi += 1
                if b0.id == a0.id:
                    ai += 1

                    pb.triangle(b1.pos, a0.pos, a1.pos)

    build_layers(pb, layers)

    def triangulate_layer(layer, order=1):
        z = layer[0].pos.z

        points = [(p.pos.x, p.pos.y) for p in layer]

        tris = polytri.triangulate(points)

        for triangle in tris:
            pb.triangle(
                *[Vec3(p[0], p[1], z) for p in triangle][::order]
            )


    triangulate_layer(layers[0], order=-1)
    triangulate_layer(layers[-1])

    return pb.build()

outer = build_object(layers[:-1])
inner = build_object(shrunk_layers[1:])

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

