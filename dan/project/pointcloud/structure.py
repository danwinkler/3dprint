import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

import visual as vi

from pointcloud import *

hscale = 300
height = 10
sections = 6
def calc( h, a ):
    offset = math.pi * .125
    angle_minus_offset = (math.pi*2 / sections) * a
    angle = angle_minus_offset + offset * h
    dist = (500 - h*30) + (150 if a % 2 == 0 else -100)
    return angle, dist

def get_layers(shrink_offset=0):
    layers = []
    for h in range( height ):
        layer = []
        for a in range( sections ):
            angle, dist = calc( h, a )
            dist -= shrink_offset
            layer.append( Vec3( math.cos( angle ) * dist, math.sin( angle ) * dist, h * 300 ) )
        layers.append( layer )
    return layers

layers = get_layers()

lines = []
for i in range(len(layers)):
    layer = layers[i]
    for j in range(len(layer)):
        p = layer[j]
        if not p:
            continue

        #To next point on layer
        p_next = layer[(j+1)%len(layer)]
        lines.append( Line(p, p_next) )

        #To point above on next layer
        if i+1 < len(layers):
            p_above = layers[i+1][j]
            lines.append( Line(p, p_above) )

        #To previous point above (Don't render)
        if i+1 < len(layers):
            p_prev_above = layers[i+1][(j-1 if j>0 else len(layer)-1)]
            lines.append( Line(p, p_prev_above) )


points = make_points_file( lines, "structure.xyz", min_bound=Vec3(-700, -700, -100 ), max_bound=Vec3( 700, 700, 3000 ), resolution=5, d=.002, r=.0006 )
