import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

import visual as vi

from pointcloud import *

objs = [
    Line( Vec3(0, 0, 0), Vec3(0, 0, 1) ),
    Line( Vec3(0, 0, 0), Vec3(1, 0, 0) ),
    Line( Vec3(0, 0, 0), Vec3(0, 1, 0) ),
]

make_points_file( objs, "lines.xyz", min_bound=Vec3(-1, -1, -1 ), max_bound=Vec3( 1.5, 1.5, 1.5 ), resolution=.03 )
