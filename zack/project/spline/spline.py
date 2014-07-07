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
y1 = [ 0, 1, 1, 1, 1, 2, 2, 2, 2, 1 ]
f1 = interp1d(x, y1, kind='cubic')

y2 = [ 0, 1, 1, 2, 2, 3, 2, 2, 2, 1 ]
f2 = interp1d(x, y2, kind='cubic')

points = []
for i in xrange(0,40):
	x = i/40.0 * 10.0
	y1 = f1( x )
	y2 = f2( x )

	points.append( [x,y1*0.8,0] )
	points.append( [x,y1,0] )

	points.append( [x,y2*0.8,1] )
	points.append( [x,y2,1] )

tris = []
for i in xrange(0,40-1):
	tris.append( [(i+0)*4+0,(i+0)*4+2,(i+1)*4+0] )
	tris.append( [(i+0)*4+2,(i+1)*4+2,(i+1)*4+0] )

	tris.append( [(i+0)*4+1,(i+0)*4+3,(i+1)*4+1] )
	tris.append( [(i+0)*4+3,(i+1)*4+3,(i+1)*4+1] )

	tris.append( [(i+0)*4+0,(i+0)*4+1,(i+1)*4+0] )
	tris.append( [(i+0)*4+1,(i+1)*4+1,(i+1)*4+0] )

	tris.append( [(i+0)*4+2,(i+0)*4+3,(i+1)*4+2] )
	tris.append( [(i+0)*4+3,(i+1)*4+3,(i+1)*4+2] )

seg = polyhedron( points=points, triangles=tris )

e = 0.037
segs = []
for r in xrange(1,100):
	segs.append(
		rotate( 5*r, [1,0,0] )(
			translate([0,exp(1.10*e*r),exp(e*r)])(
				scale( [0.8*exp(e*r), 1.6*exp(e*r), 0.6*exp(e*r)] )(
					seg
				)
			)
		)
	)

all = union()(
	segs
)

scad_render_to_file(
	all, "spline.scad"
)
