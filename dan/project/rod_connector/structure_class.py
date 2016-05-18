import sys
sys.path.append( "../../../" )
from dan.lib.helper import *

class LayerStructure:
    def get_layers(self, shrink_offset=0):
        layers = []
        for h in range( self.height ):
            layer = []
            for a in range( self.sections ):
                angle, dist = self.calc( h, a )
                dist -= shrink_offset
                layer.append( Vec3( math.cos( angle ) * dist, math.sin( angle ) * dist, h * 300 ) )
            layers.append( layer )
        return layers
