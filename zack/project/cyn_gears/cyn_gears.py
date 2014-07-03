from solid import *
import random
import sys
from math import *
from random import *

sys.path.append( "../../../" )
from zack.lib.mat import *
from zack.lib.pathmat import *



def radialFunc( i, heightSegCount, j, radialSegCount ):
	t = 3.14 * 2.0 * float(j) / float(radialSegCount)
	radius = 10
	n = 2.0 * 3.14 * 16 * j / radialSegCount
	return Vec3( [ (1.2 * sin(n) + radius) * cos(t), (1.2 * sin(n) + radius) * sin(t), 0 ] )


path = [ Vec3([1,0,0]), Vec3([1,0,1]) ]
pathMat = pathToPathMat( path )

all = extrudeTubeAlongPath( 128, len(pathMat), pathMat, 10, radialFunc )

scad_render_to_file(
	all, "cyn_gears.scad"
)


