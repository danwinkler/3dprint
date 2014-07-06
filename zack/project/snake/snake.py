from solid import *
import random
import sys
from math import *
from random import *

sys.path.append( "../../../" )
from zack.lib.mat import *
from zack.lib.pathmat import *


path = []
for i in xrange(0,32):
	t = float(i) / 32.0 * 3.14 * 2.0 * (2.0 / 3.0)
	path.append( Vec3( [ 50 * cos(t), 50 * sin(t), 0 ] ) )

pathMat = pathToPathMat( path )
tube = extrudeTubeAlongPath( 32, len(pathMat), pathMat, 10 )



tab_height = 10
tab_width = 6
hole_height = 3
cyl_height = 30

tab = translate( [6,-tab_width/2,cyl_height] )(
	cube( [ 2, tab_width, tab_height+hole_height ] ),
	hull()(
		translate( [4,+tab_width,tab_height] )(
		rotate( 90, [1,0,0] )(
			cylinder( r=0.1, h=tab_width )
		)),
	
		translate( [2,+tab_width,tab_height] )(
		rotate( 90, [1,0,0] )(
			cylinder( r=0.1, h=tab_width )
		)),
	
		translate( [2,+tab_width,tab_height+3] )(
		rotate( 90, [1,0,0] )(
			cylinder( r=0.1, h=tab_width )
		))
	)
)

whole = union() (
	difference()(
		cylinder( r=10, h=cyl_height ),
		#translate([0,0,12])( cylinder( r1=9, r2=5, h=15 ) ),
		translate([0,0,-1])( cylinder( r=9, h=cyl_height/2 ) ),
		translate([-15,-tab_width/2,tab_height])( cube( [30,tab_width,hole_height] ) )
	),
	intersection()(
		translate([0,0,cyl_height])( cylinder( r=8.5, h=8 ) ),
		translate([-5,-10,cyl_height])( cube( [10,20,10] ) )
	),
	tab,
	scale([-1,1,1])( tab )
)

top = translate( [0,0,-15] )(
	intersection()(
		whole,
		translate( [ -15, -15, 15 ] )( cube( [ 30, 30, 30 ] ) )
	)
)

bottom = translate( [0,0,15] )(
	rotate( 180, [1,0,0] )(
		intersection()(
			whole,
			translate( [ -10, -10, 0 ] )( cube( [ 20, 20, 15 ] ) )
		)
	)
)

t = 3.14 * 2.0 * (2.0 / 3.0)
all = union()(
	tube,
	translate([50,2,0])( rotate( 90, [1,0,0] )( top ) ),
	translate([51*cos(t)-10,51*sin(t)+9,0])( rotate( 49, [0,0,1] )( rotate( 90, [1,0,0] )( bottom ) ) )
)


scad_render_to_file(
	all, "snake.scad"
)


