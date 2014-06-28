from solid import *
import random
import sys
from math import *

sys.path.append( "../../../" )
from zack.lib.mat import *


balls = []
_t = 0
for t in range(0,1000):
	_t += exp( -0.0001 * t )
	m = Mat4()
	m.cat( trans3D( [0.1*_t,0,0] ) )
	m.cat( rotate3D( [0,0,1], _t ) )
	p = m.mul( [ 1, 0, _t*0.1 ] )

	a = sphere( 2, segments=10 )
	balls.append( translate(p.list())(a) )


scad_render_to_file(
	difference()(
		cylinder(r1=0, r2=50, h=50),
		translate([0,0,2])(
			cylinder(r1=0, r2=50, h=50)
		),
		translate([0,0,1])(
			balls
		),
		cylinder(r=10,h=60)
	), "lampshade.scad"
)


