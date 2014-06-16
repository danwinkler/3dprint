import sys
sys.path.append( "../../../" )

import math
import random

from solid import *
from solid.utils import *

parts = []

parts.append( cylinder( r=10, h=40 ) )

print "Saving File"
with open( __file__ + ".scad", "w" ) as f:
	f.write( scad_render( union()( parts ) ) )