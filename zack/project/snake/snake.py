from solid import *
import random
import sys
from math import *
from random import *

sys.path.append( "../../../" )
from zack.lib.mat import *
from zack.lib.pathmat import *

tab_height = 10
tab_width = 6
hole_height = 3
cyl_height = 30
female_thickness = 2
radius = 7.5

path = []
for i in xrange(0,32):
	t = float(i) / 32.0 * 3.14 * 2.0 * (2.0 / 3.0)
	path.append( Vec3( [ 50 * cos(t), 50 * sin(t), 0 ] ) )

pathMat = pathToPathMat( path )
tube = extrudeTubeAlongPath( 32, len(pathMat), pathMat, radius )


tab = translate( [10-female_thickness-3,-tab_width/2,cyl_height] )(
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

whole0 = difference()(
	union() (
		difference()(
			# Female outside
			cylinder( r=10, h=cyl_height ),

			# Female inside
			translate([0,0,-1])( cylinder( r=10-female_thickness, h=cyl_height/2 ) ),

			# Tab holes
			translate([-15,-tab_width/2,tab_height])( cube( [30,tab_width,hole_height] ) )
		),

		# Male insert
		intersection()(
			translate([0,0,cyl_height])( cylinder( r=10-female_thickness-0.5, h=8 ) ),
			translate([-5+female_thickness/2,-10,cyl_height])( cube( [10-female_thickness,20,10] ) )
		),

		# Tabs
		tab,
		scale([-1,1,1])( tab )
	),
	translate([0,0,13])( cylinder( r2=0, r1=10-female_thickness, h=15 ) )
)

whole1 = difference()(
	union() (
		difference()(
			# Female outside
			cylinder( r=10, h=cyl_height ),

			# Female inside
			translate([0,0,-1])( cylinder( r=10-female_thickness, h=cyl_height/2 ) )
		),

		translate([0,0,cyl_height])( cylinder( r=10-female_thickness-0.5, h=8 ) )
	),
	translate([0,0,13])( cylinder( r2=0, r1=10-female_thickness, h=15 ) )
)

whole = difference()(
	cylinder( r=radius, h=30 ),
	translate([-radius,0,-1])( cube( [ 20, 20, 20 ] ) ),
	translate([0,18,9])( rotate(90,[1,0,0])( cylinder( r=2, h=30 ) ) ),
	translate([0,-radius+2.5,9])( rotate(90,[1,0,0])( cylinder( r=3.5, h=2.5, segments=6 ) ) )
)

t = 3.14 * 2.0 * (2.0 / 3.0)
parity = 180
all = union()(
	tube,
	translate([50,-24,0])( rotate( -90, [1,0,0] )( rotate( parity, [0,0,1] )( whole ) ) ),
	translate([51*cos(t)+8,51*sin(t)-6,0])( rotate( 180+49, [0,0,1] )( rotate( 90, [1,0,0] )( rotate( parity, [0,0,1] )( whole ) ) ) )
)

scad_render_to_file(
	all, "snake.scad"
)


