import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

import numpy as np

import visual as vi

class Point:
    def __init__(self, x, y, z):
        self.pos = Vec3()
        self.set( x, y, z )

    def set(self, x, y, z):
        self.pos.x = x
        self.pos.y = y
        self.pos.z = z

    def render(self):
        self.sphere = vi.sphere(pos=self.pos.to_list(), radius=.1)

    def distance( self, point ):
        return self.pos.distance( point )

    def __repr__(self):
        return self.pos.__repr__()


class Line:
    def __init__(self, p0, p1):
        self.p0 = p0.copy()
        self.p1 = p1.copy()

    def render(self):
        self.curve = vi.curve()
        self.curve.append( pos=self.p0.to_list() )
        self.curve.append( pos=self.p1.to_list() )

    def distance( self, point ):
        return point_to_line_segment( point, self.p0, self.p1 )

    def __repr__(self):
        return self.pos.__repr__()

def force_function( distance ):
    if distance == 0:
        return 0
    f = ((1.0/(distance ** 2)))
    return f

def get_points( objs, min_bound=Vec3(-1,-1,-1), max_bound=Vec3(1,1,1), resolution=.05, d=12, range=1, force_function=force_function ):
    points = []
    for x in np.arange( min_bound.x, max_bound.x, resolution ):
        print x
        for y in np.arange( min_bound.y, max_bound.y, resolution ):
            for z in np.arange( min_bound.z, max_bound.z, resolution ):
                p = Vec3( x, y, z )
                v = 0
                for o in objs:
                    v += force_function( o.distance( p ) )
                r_min = d - range*.5
                r_max = d + range*.5
                if v > r_min and v < r_max:
                    points.append( Point( x, y, z ) )
    return points

def write_points( points, filename ):
    vecs = [f.pos for f in points]
    string_out = "\n".join( [" ".join( [str(v) for v in f.to_list()] ) for f in vecs] )
    with open( filename, "w" ) as f:
        f.write( string_out )
