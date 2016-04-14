'''
import pyglet
from pyglet.gl import *

window = pyglet.window.Window()

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(window.width, 0)
    glVertex2f(window.width, window.height)
    glEnd()

pyglet.app.run()
'''

import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

layer_count = 10
rot_count = 6
offset = math.pi * .125

layers = []
points = []
connectors = []

#Create points
for h in range( layer_count ):
    layer = []
    for a in range( rot_count ):
        angle_minus_offset = (math.pi*2 / rot_count) * a
        angle = angle_minus_offset + offset * h
        #dist = (500 - h*30) + math.cos( angle_minus_offset * 2 ) * 150 #Variation A
        #dist = (500 - h*30) + math.cos( angle_minus_offset ) * 200 #Variation B
        #dist = (500 - h*30) - math.cos( angle_minus_offset * 2 ) * 150 #Variation C
        #dist = (500 - h*30) + (100 if a % 3 == 0 else 0) #Variation D
        #dist = (500 - h*30) + (150 if a % 2 == 0 else -100) #Variation E
        dist = (500 - h*30)
        layer.append( Vec3( math.cos( angle ) * dist, math.sin( angle ) * dist, h * 300 ) )
    layers.append( layer )

parts = []

#Create connectors
for i in range(len(layers)):
    layer = layers[i]
    for j in range(len(layer)):
        p = layer[j]

        #To next point on layer
        p_next = layer[(j+1)%len(layer)]
        next_vec = p_next.copy()
        next_vec -= p
        parts.append( translate( p.to_list() ) ( cyl_on_vec( next_vec, r=10 ) ) )

        #To point above on next layer
        if i+1 < len(layers):
            p_above = layers[i+1][j]
            above_vec = p_above.copy()
            above_vec -= p
            parts.append( translate( p.to_list() ) ( cyl_on_vec( above_vec, r=10 ) ) )

        #To next point on lower layer
        if i > 0:
            p_below = layers[i-1][(j+1)%len(layer)]
            below_vec = p_below.copy()
            below_vec -= p
            parts.append( translate( p.to_list() ) ( cyl_on_vec( below_vec, r=10 ) ) )

        parts.append( translate( p.to_list() ) ( sphere( 30 ) ) )

print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
	f.write( scad_render( union()( parts ) ) )
