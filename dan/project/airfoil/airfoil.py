import sys
sys.path.append( "../../../" )
from dan.lib.helper import *
from dan.lib.naca import *

import math
import random

from solid import *
from solid.utils import *

parts = []

#Symmetrical 4-digit naca airfoil
def thickness( x, c, t ):
	x = float(x)
	c = float(c)
	t = float(t)
	p1 = .2969*math.sqrt(x/c)
	p2 = -.1260*(x/c)
	p3 = -.3516*((x/c)**2)
	p4 = .2843*((x/c)**3)
	p5 = -.1015*((x/c)**4)
	return (t/.2)*c*(p1+p2+p3+p4+p5)
	
points = []
paths = []

#for x in range( 20 ):
#	points.append( [x, thickness(x, 20, .2 )] )

wing_rez = 15

points = naca5( "23116", wing_rez )

def ff( height, a ):
	angle = a * math.pi * 2
	#d = 1 - min( 1 / (height+.1)*.1, 2 )
	d = thickness( height*20, 20, .1 )
	return math.cos( angle ) * d, math.sin( angle ) * d, height * 20

def pf( height, i ):
	scale = 4.5-(1.0 / ((20-height)*2))*4
	return [(points[i][0]-.8)*scale, points[i][1]*scale, height*.5]

def wing():
	return make_trunk( 20, wing_rez*2, pf, index=True )

#WINGS
parts.append( rotate( 90, [1, 0,0] ) ( wing() ) )
parts.append( mirror( [0,1,0] ) ( rotate( 90, [1, 0,0] ) ( wing() ) ) )

#TAIL
parts.append( translate( [10,0,0] ) ( scale( .5 ) ( union() (
	rotate( 90, [1, 0,0] ) ( wing() ) ,
	mirror( [0,1,0] ) ( rotate( 90, [1, 0,0] ) ( wing() ) ),
	scale( [1,1,.5] ) ( rotate( 0, [1, 0,0] ) ( wing() )  )
))))


#FUSELAGE
parts.append( 
	translate( [-7,0,0] ) ( 
		rotate( 90, [0,1,0] ) ( 
			make_trunk( 20, 10, ff ) 
		) 
	) 
)
	
#path = []
#for i in range( len( points ) ):
#	path.append( i )
#paths.append( path )
#shape = scale( 10 ) ( polygon( points, paths ) )
#parts.append( linear_extrude( height=5 )( shape ) )

print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
	f.write( scad_render( union()( parts ) ) )