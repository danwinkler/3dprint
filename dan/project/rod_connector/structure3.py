import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random
import time

from solid import *
from solid.utils import *

import connector as conn
import layer_structure

layer_count = 10
rot_count = 6
offset = math.pi * .125

layers = []

#Create points
for h in range( layer_count ):
    layer = []
    for a in range( rot_count ):
        angle_minus_offset = (math.pi*2 / rot_count) * a
        angle = angle_minus_offset + offset * h
        dist = (500 - h*30) + math.cos( angle_minus_offset ) * 200 #Variation B
        #dist = (500 - h*30) - math.cos( angle_minus_offset * 2 ) * 150 #Variation C
        #dist = (500 - h*30) + (100 if a % 3 == 0 else 0) #Variation D
        #dist = (500 - abs(h)*30)

        #For door
        if False and h < 4 and h > 0 and a == 0:
            layer.append( None )
        else:
            layer.append( Vec3( math.cos( angle ) * dist, math.sin( angle ) * dist, h * 300 ) )
    layers.append( layer )

parts = layer_structure.create_from_layers( layers )

print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
	f.write( scad_render( union()( parts ) ) )
