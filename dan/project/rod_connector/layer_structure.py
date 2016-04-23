import sys
sys.path.append( "../../../" )

from dan.lib.helper import *

import math
import random
import time

from solid import *
from solid.utils import *

import connector as conn

def create_from_layers( layers, save_name=None ):
    parts = []
    connectors = []
    for i in range(len(layers)):
        layer = layers[i]
        for j in range(len(layer)):
            p = layer[j]
            if not p:
                continue
            connector = []

            #To next point on layer
            p_next = layer[(j+1)%len(layer)]
            if p_next:
                next_vec = p_next.copy()
                next_vec -= p
                parts.append( translate( p.to_list() ) ( cyl_on_vec( next_vec, r=10 ) ) )
                connector.append( next_vec )

            #To previous point on layer (don't render)
            p_prev = layer[(j-1 if j>0 else len(layer)-1)]
            if p_prev:
                prev_vec = p_prev.copy()
                prev_vec -= p
                connector.append( prev_vec )

            #To point above on next layer
            if i+1 < len(layers):
                p_above = layers[i+1][j]
                if p_above:
                    above_vec = p_above.copy()
                    above_vec -= p
                    parts.append( translate( p.to_list() ) ( cyl_on_vec( above_vec, r=10 ) ) )
                    connector.append( above_vec )

            #To previous point above (Don't render)
            if i+i < len(layers):
                p_prev_above = layers[i+1][(j-1 if j>0 else len(layer)-1)]
                if p_prev_above:
                    prev_above_vec = p_prev_above.copy()
                    prev_above_vec -= p
                    connector.append( prev_above_vec )

            #To next point on lower layer
            if i > 0:
                p_next_below = layers[i-1][(j+1)%len(layer)]
                if p_next_below:
                    next_below_vec = p_next_below.copy()
                    next_below_vec -= p
                    parts.append( translate( p.to_list() ) ( cyl_on_vec( next_below_vec, r=10 ) ) )
                    connector.append( next_below_vec )

            #To point below (Don't render)
            if( i > 0 ):
                p_below = layers[i-1][j]
                if p_below:
                    below_vec = p_below.copy()
                    below_vec -= p
                    connector.append( below_vec )

            parts.append( translate( p.to_list() ) ( sphere( 30 ) ) )
            connectors.append( connector )

    if save_name:
        directory = "designs/" + save_name
        if not os.path.exists(directory):
            os.makedirs(directory)

        for i in range(len(connectors)):
            with open( directory + "/" + str(i) + ".scad", "w" ) as f:
                f.write( scad_render( conn.connector( connectors[i] ) ) )

    return parts
