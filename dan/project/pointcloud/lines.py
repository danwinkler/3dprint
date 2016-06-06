import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

import visual as vi

lines = []

lines.append( [Vec3(0, 0, 0), Vec3(0, 1, 0)])
lines.append( [Vec3(0, 0, 0), Vec3(1, 0, 0)])

def draw_line( line ):
    c = vi.curve()
    c.append(pos=line[0].to_list())
    c.append(pos=line[1].to_list())

for line in lines:
    draw_line( line )

for i in range( 1000 ):
    p = Vec3( random.uniform( -1, 2 ), random.uniform( -1, 2 ), random.uniform( -1, 2 ) )
    good = False
    for line in lines:
        v = point_to_line_segment( p, line[0], line[1] )
        if v > .3 and v < .5:
            good = True

    if good:
        vi.sphere( pos=p.to_list(), radius=.05 )
