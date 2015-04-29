import sys
sys.path.append( "../../../" )

import math
import random

from dan.lib.traceprint_python import *

parts = []

parts.append( cylinder( 10, 40 ) )

print "Saving File"
write_out( __file__ + ".json", union( *parts ) )