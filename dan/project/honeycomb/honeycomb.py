import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

from scipy.spatial import Voronoi

points = []
for y in range( 20 ):
    for x in range( 10 ):
        offset = 0 if y % 2 == 0 else .5
        points.append( Vec3( x + offset, y ) )

axis = Vec3( 0, 0, 1 )
angle = math.pi * .2

for y in range( 20 ):
    for x in range( 10 ):
        offset = 0 if y % 2 == 0 else .5
        offset -= 5
        p = Vec3( x + offset, y )
        p = p.rotate( axis, angle )
        points = filter( lambda tp: tp.distance2( p ) > (.5*.5), points )
        points.append( p )

vor = Voronoi( [p.to_list()[:2] for p in points] )

#Remove incomplete regions
regions = filter(lambda x: all(i >= 0 for i in x) and len(x) > 0, vor.regions)

def area(corners):
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

#Remove too big regions
regions = filter(lambda region: area([vor.vertices[r] for r in region]) < 3, regions)

#Assemble extruded sections
parts = []
for region in regions:
    h = random.uniform(.5, 1.5)
    h=1

    verts = [vor.vertices[r] for r in region]

    verts_vec = [Vec3(vert[0], vert[1]) for vert in verts]

    avg_point = Vec3( sum([v.x for v in verts_vec]), sum([v.y for v in verts_vec]) )
    avg_point /= len(verts_vec)

    p2 = []

    for v in verts_vec:
        vec = Vec3( v.x, v.y )
        vec -= avg_point
        vec *= .8
        vec += avg_point
        p2.append( vec )

    parts.append(
        linear_extrude( height=h ) (
            polygon( points=[[v[0], v[1]] for v in verts] )
        ) - down( 1 ) ( linear_extrude( height=h+2 ) (
            polygon( points=[v.to_list()[:2] for v in p2] )
        ) )
    )

print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
    f.write( scad_render( union() ( parts ) ) )
