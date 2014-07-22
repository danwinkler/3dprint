from solid import *
import random
import sys
from math import *
from random import *

sys.path.append( "../../../" )
from zack.lib.mat import *
from zack.lib.pathmat import *

import numpy as np
from scipy.interpolate import interp1d

x = np.linspace(0, 10, 10)
#y1 = [ 0, 1, 1, 1, 1, 2, 2, 2, 2, 1 ]
y1 = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
f1 = interp1d(x, y1, kind='cubic')

#y2 = [ 0, 1, 1, 2, 2, 3, 2, 2, 2, 1 ]
y2 = [ 2, 2, 2, 2, 2, 3, 2, 2, 2, 2 ]
f2 = interp1d(x, y2, kind='cubic')

def rev( flip, list ):
	if flip == 1:
		return [ list[2], list[1], list[0] ]
	return list

x_range = 40
points = []
for i in xrange(0,x_range):
	x = i/float(x_range) * 10.0
	y1 = f1( x )
	y2 = f2( x )

	points.append( [x,y1*0.3,0] )
	points.append( [x,y1,0] )

	points.append( [x,y2*0.3,1] )
	points.append( [x,y2,1] )

tris = []
for i in xrange(0,x_range-1):
	tris.append( rev( 1, [(i+1)*4+0,(i+0)*4+2,(i+0)*4+0] ) )
	tris.append( rev( 1, [(i+1)*4+0,(i+1)*4+2,(i+0)*4+2] ) )

	tris.append( rev( 1, [(i+0)*4+1,(i+0)*4+3,(i+1)*4+1] ) )
	tris.append( rev( 1, [(i+0)*4+3,(i+1)*4+3,(i+1)*4+1] ) )

	tris.append( rev( 1, [(i+0)*4+0,(i+0)*4+1,(i+1)*4+0] ) )
	tris.append( rev( 1, [(i+0)*4+1,(i+1)*4+1,(i+1)*4+0] ) )

	tris.append( rev( 0, [(i+0)*4+2,(i+0)*4+3,(i+1)*4+2] ) )
	tris.append( rev( 0, [(i+0)*4+3,(i+1)*4+3,(i+1)*4+2] ) )

tris.append( rev( 1, [2,1,0] ) )
tris.append( rev( 1, [3,1,2] ) )

tris.append( rev( 1, [(x_range-1)*4+0,(x_range-1)*4+1,(x_range-1)*4+2] ) )
tris.append( rev( 0, [(x_range-1)*4+3,(x_range-1)*4+1,(x_range-1)*4+2] ) )

seg = polyhedron( points=points, triangles=tris )

e = 0.037
segs = []
for r in xrange(1,100):
	segs.append(
		rotate( 15*r, [1,0,0] )(
			translate([9*exp(1.10*e*r),8*exp(1.10*e*r),2.6*exp(e*r)])(
				scale( [4.8*exp(e*r), 7.6*exp(e*r), 10*exp(e*r)] )(
					seg
				)
			)
		)
	)

all = difference()(
	union()(
		segs
	),
	translate([+1600,-1500,-1500])( cube([3000,3000,3000]) )
)

scad_render_to_file(
	segs[0], "spline.scad"
)
