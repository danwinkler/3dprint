from solid import *
import random
import sys
from math import *
from random import *

sys.path.append( "../../../" )
from zack.lib.mat import *
from zack.lib.pathmat import *


leaf = union()(
	rotate( +25, [0,1,0] )( hull()(
		translate( [0,0,0] )( sphere(r=1) ),
		translate( [-6,6,0] )( sphere(r=1) ),
		translate( [0,20,0] )( sphere(r=1) )
	)),
	rotate( -25, [0,1,0] )( hull()(
		translate( [0,0,0] )( sphere(r=1) ),
		translate( [+6,6,0] )( sphere(r=1) ),
		translate( [0,20,0] )( sphere(r=1) )
	))
)


scad_render_to_file(
	leaf, "leafy.scad"
)


