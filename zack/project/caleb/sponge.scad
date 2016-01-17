

difference() {
	cube(size = [10, 10, 0.2000000000]);
	cylinder(h = 5, r = 5);
}
/***********************************************
******      SolidPython code:      *************
************************************************
 
from solid import *
from random import *
from math import *
import sys
import copy

sys.path.append( "../../../" )
from zack.lib.mat import *
from zack.lib.pathmat import *


sponge = difference()(
	cube([10,10,0.2]),
	cylinder( r=5, h=5 )
)

scad_render_to_file(
	sponge, "sponge.scad"
)
 
 
***********************************************/
                            
