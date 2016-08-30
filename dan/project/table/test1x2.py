import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

inner_x = 19
inner_y = 38

height = 20

offset = .1
offsets = [.05,.1,.15]

wall_thickness = 4

parts = []

base_width = (wall_thickness + inner_x) * len(offsets) + wall_thickness + sum( offsets )*2
b = cube( [base_width,inner_y+wall_thickness*2+(max(offsets)*2), height] )

offset_accum = wall_thickness
for i, o in enumerate(offsets):
    x_off = offset_accum
    b -= translate( [ x_off, wall_thickness, 0] ) (
        cube( [inner_x+o*2, inner_y+o*2, height] )
    )
    offset_accum += inner_x + o*2 + wall_thickness


parts += [b]

print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
    f.write( scad_render( union() ( parts ) ) )
