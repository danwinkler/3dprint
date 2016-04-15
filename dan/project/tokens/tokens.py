import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

def make_token():
    token = cylinder( r=20, h=6 )
    token -= down( 1 ) ( cylinder( r=18, h=3 ) )
    token -= up( 4 ) ( cylinder( r=21, h=3 ) - cylinder( r=17.5, h=3 ) )
    return token

def plus_one():
    return linear_extrude( height=3 ) ( text( "+1", size=16, valign="center", halign="center" ) )

def neg_one():
    return linear_extrude( height=3 ) ( text( "-1", size=16, valign="center", halign="center" ) )

def poison():
    return dxf_linear_extrude( "Symbols.dxf" )

funs = [
    plus_one,
    neg_one,
    poison
]

for f in funs:
    token = make_token()
    token -= translate( [0,0,4] ) (
        f()
    )

    print "Saving " + f.__name__
    with open( f.__name__ + ".scad", "w" ) as f:
        f.write( scad_render( token ) )
