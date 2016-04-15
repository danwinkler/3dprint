import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random

from solid import *
from solid.utils import *

def make_token():
    token = cylinder( r=20, h=6, segments=36 )
    token -= down( 1 ) ( cylinder( r=18, h=3, segments=36 ) )
    token -= up( 4 ) ( cylinder( r=21, h=3, segments=36 ) - cylinder( r=17.5, h=3, segments=36 ) )
    return token

def plus_one():
    return linear_extrude( height=3 ) ( text( "+1", size=16, valign="center", halign="center" ) )

def neg_one():
    return linear_extrude( height=3 ) ( text( "-1", size=16, valign="center", halign="center" ) )

def poison():
    return linear_extrude( height=3 ) ( text( "\uE618", size=16, font="mana", valign="center", halign="center" ) )

def white():
    return linear_extrude( height=3 ) ( text( "\uE600", size=16, font="mana", valign="center", halign="center" ) )

def blue():
    return linear_extrude( height=3 ) ( text( "\uE601", size=16, font="mana", valign="center", halign="center" ) )

def black():
    return linear_extrude( height=3 ) ( text( "\uE602", size=16, font="mana", valign="center", halign="center" ) )

def red():
    return linear_extrude( height=3 ) ( text( "\uE603", size=16, font="mana", valign="center", halign="center" ) )

def green():
    return linear_extrude( height=3 ) ( text( "\uE604", size=16, font="mana", valign="center", halign="center" ) )

funs = [
    plus_one,
    neg_one,
    poison,
    white,
    blue,
    black,
    red,
    green
]

for f in funs:
    token = make_token()
    token -= translate( [0,0,4] ) (
        f()
    )

    print "Saving " + f.__name__
    with open( f.__name__ + ".scad", "w" ) as f:
        f.write( scad_render( token ) )
