from solid import *
import random
import sys
from math import *
from random import *

sys.path.append( "../../../" )
from zack.lib.mat import *
from zack.lib.pathmat import *



cubic_spline( p1, p2, p1d, p2d ):
	// Solve for the 2D spline coef.  The z value of the verts is ignored.
	a = Vec3()
	b = Vec3()
	c = Vec3()
	d = Vec3()
	a.x =   2*p1.x +  -2*p2.x +   1*p1d.x +   1*p2d.x;
	a.y =   2*p1.y +  -2*p2.y +   1*p1d.y +   1*p2d.y;

	b.x =  -9*p1.x +   9*p2.x +  -5*p1d.x +  -4*p2d.x;
	b.y =  -9*p1.y +   9*p2.y +  -5*p1d.y +  -4*p2d.y;

	c.x =  12*p1.x + -12*p2.x +   8*p1d.x +   5*p2d.x;
	c.y =  12*p1.y + -12*p2.y +   8*p1d.y +   5*p2d.y;

	d.x =  -4*p1.x +   5*p2.x +  -4*p1d.x +  -2*p2d.x;
	d.y =  -4*p1.y +   5*p2.y +  -4*p1d.y +  -2*p2d.y;

	return a, b, c, d


path = [ Vec3([0,0,0]), Vec3([1,1,0]), Vec3([2,1,0]), Vec3([3,2,0]) ]
for i in path:
	
	cubic_spline( p1, p2, p1d, p2d ):



			float splineStep = Cald_splineStep;
			float lastX = 0.f;
			float lastY = 0.f;
			for( float j=1.f; j<=2.f; j+=splineStep ) {

				float x = result[0].x * j*j*j + result[1].x * j*j + result[2].x * j + result[3].x;
				float y = result[0].y * j*j*j + result[1].y * j*j + result[2].y * j + result[3].y;

				if( j > 1.f ) {
					float dx = x - lastX;
					float dy = y - lastY;
				}

				shapePoints.add( FVec3(x,y,0.f) );

				lastX = x;
				lastY = y;
			}
