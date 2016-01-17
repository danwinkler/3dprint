from solid import *
from random import *
from math import *
import sys
import copy

sys.path.append( "../../../" )
from zack.lib.mat import *
from zack.lib.pathmat import *

spheres = []
for i in xrange(0,100):
	spheres.append( translate([10*cos(i/80.0),10*sin(i/100.0),0])( sphere(r=1) ) )


all = union()(
	spheres
)

scad_render_to_file(
	all, "caleb3.scad"
)
