import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

#Small desktop water fountain
#Ordered small water pump from amazon
#Rotating part at top of fountain that, when spins, alternates blocking some of the holes for the water to spray out of
# So that you get like an alternating patten of water spraying out of the top

parts = []

parts.append( cylinder( 10, 40 ) )

print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
    f.write( scad_render( union() ( parts ) ) )
