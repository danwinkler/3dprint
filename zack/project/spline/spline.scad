

union();
/***********************************************
******      SolidPython code:      *************
************************************************
 
from solid import *
import random
import sys
from math import *
from random import *

sys.path.append( "../../../" )
from zack.lib.mat import *
from zack.lib.pathmat import *
from zack.lib.pycurve import *

P = [ (0,0), (1,1), (2,1), (3,2), (4,5) ]

n = len(P) - 1
k = 3
m = n + k + 1
_t = 1 / (m - k * 2)
t = k * [0] + [t_ * _t for t_ in xrange(m - (k * 2) + 1)] + [1] * k

S = Bspline( P, t, k )

for i in xrange(0,10):
	t_ = i / 10.0

	try:
		x, y = S(t_)
	except:
		print "skip"
		continue

	print x, y


scad_render_to_file(
	union()(), "spline.scad"
)


 
 
***********************************************/
                            
