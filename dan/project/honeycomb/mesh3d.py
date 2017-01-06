import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

from scipy.spatial import Voronoi

random.seed( 0 )

x_size = 100
y_size = 100
z_size = 100

num_points = 100
min_dist = 5
min_dist2 = min_dist**2

r = .3


points = []

while len(points) < num_points:
    p = Vec3( random.uniform( 0, x_size ), random.uniform( 0, y_size ), random.uniform( 0, z_size ) )
    if all(op.distance2( p ) > min_dist2 for op in points):
        points.append( p )

vor = Voronoi( [p.to_list() for p in points] )

parts = []

class PointObj:
    def __init__( self, p ):
        self.ridges = []
        self.p = p

class RidgeObj:
    def __init__( self, p0, p1 ):
        self.p0 = p0
        self.p1 = p1

point_list = [PointObj( Vec3(v[0], v[1], v[2])) for v in vor.vertices]

for ridge in vor.ridge_vertices:
    if ridge[0] == -1 or ridge[1] == -1:
        continue

    for i in range(len(ridge)-1):
        p0 = point_list[ridge[i]]
        p1 = point_list[ridge[i+1]]
        r = Ridge( p0, p1 )
        p0.ridges.append( r )
        p1.ridges.append( r )

for ridge in vor.ridge_vertices:
    if ridge[0] == -1 or ridge[1] == -1:
        continue

    for i in range(len(ridge)-1):
        p0 = vor.vertices[ridge[i]]
        p1 = vor.vertices[ridge[i+1]]

        if p0[0] < 0 or p0[0] > x_size or p0[1] < 0 or p0[1] > y_size or p0[2] < 0 or p0[2] > z_size:
            continue

        if p1[0] < 0 or p1[0] > x_size or p1[1] < 0 or p1[1] > y_size or p1[2] < 0 or p1[2] > z_size:
            continue

        vec = Vec3( p0[0], p0[1], p0[2] )
        vec.x -= p1[0]
        vec.y -= p1[1]
        vec.z -= p1[2]

        parts.append( translate( [p1[0], p1[1], p1[2]] ) ( cyl_on_vec( vec, r=r ) ) )
        parts.append( translate( [p0[0], p0[1], p0[2]] ) ( sphere( r=r*1, segments=12 ) ) )

print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
    f.write( scad_render( union() ( parts ) ) )
