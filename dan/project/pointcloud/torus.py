import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

import visual as vi

class Point:
    def __init__(self, x, y, z):
        self.pos = Vec3()
        self.obj = vi.sphere(radius=.1)
        self.set( x, y, z )

    def set(self, x, y, z):
        self.pos.x = x
        self.pos.y = y
        self.pos.z = z
        self.obj.pos.x = x
        self.obj.pos.y = y
        self.obj.pos.z = z

    def __repr__(self):
        return self.pos.__repr__()

followers = []
points = []
for i in range( 12 ):
    a = (i / 12.0) * math.pi * 2
    points.append( Point( math.cos( a )*2, math.sin( a ), 0 ) )

for i in range( 50 ):
    dist = 3
    f = Point( random.uniform( -dist, dist ), random.uniform( -dist, dist ), random.uniform( -dist, dist ) )
    followers.append( f )

A = .01
B = -.1
f_max = .5
f_min = -.5
def force_function( distance2 ):
    if distance2 == 0:
        return 0
    f = (A * (1.0/(distance2 ** 2)) + B) * .01
    f = max( min( f, f_max ), f_min )
    return f

FA = .3
FB = .1
def friend_force( distance2 ):
    f = -FA * (distance2 ** 2) + FB
    f = max( min( f, f_max ), f_min )
    return f

for i in range( 20 ):
    print i / 10.0, force_function( i / 10.0 )

dt = .5
while( True ):
    vi.rate( 120 )
    for f in followers:
        force = Vec3()
        for p in points:
            v = f.pos - p.pos
            mag = v.length()
            v /= mag #to normalize
            _force = force_function( mag )
            v *= _force
            force += v

        for o in followers:
            if o is f:
                continue
            v = f.pos - o.pos
            mag = v.length()
            v /= mag #to normalize
            _force = force_function( mag )
            if _force < 0: continue
            v *= _force
            force += v

        #if force.length2() > .1 ** 2:
        #    force.normalize()
        #    force *= .1

        force *= dt

        f.set( f.pos.x + force.x, f.pos.y + force.y, f.pos.z + force.z )
