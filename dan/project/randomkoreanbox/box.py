import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

from dan.lib.plan import *

import math
import random

from solid import *
from solid.utils import *

circuit_board_size = Vec3(50, 20) #TODO: set

box_inner_size = circuit_board_size.copy()
box_inner_size.z = 30 #TODO: set
box_inner_size += (2, 2, 0) # Margin around circuit board

wall_thickness=3

class ScrewHoleBlock(Part):
    block = CubePart(10, 10, 10)

class KoreanBox(Part):
    box = Box(
        box_inner_size.x+wall_thickness*2,
        box_inner_size.y+wall_thickness*2,
        box_inner_size.z+wall_thickness*2,
        bottom=wall_thickness,
        left=wall_thickness,
        right=wall_thickness,
        front=wall_thickness,
        back=wall_thickness,
        top=0,
        roundover=1.5
    )

    screw_hole_a = box.place_in_corner(ScrewHoleBlock(), 0, 0, 0)
    screw_hole_b = box.place_in_corner(ScrewHoleBlock(), 1, 0, 0)
    screw_hole_c = box.place_in_corner(ScrewHoleBlock(), 1, 1, 0)
    screw_hole_d = box.place_in_corner(ScrewHoleBlock(), 0, 1, 0)

kbox = KoreanBox()

kbox.render( __file__ + ".scad" )
