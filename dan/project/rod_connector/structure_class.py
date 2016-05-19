import sys
import random
import math

from scipy.spatial import Delaunay

sys.path.append( "../../../" )
from dan.lib.helper import *
from solid import *
from solid.utils import *

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

ASCII_FACET = """facet normal 0 0 0
outer loop
vertex {face[0][0]:.4f} {face[0][1]:.4f} {face[0][2]:.4f}
vertex {face[1][0]:.4f} {face[1][1]:.4f} {face[1][2]:.4f}
vertex {face[2][0]:.4f} {face[2][1]:.4f} {face[2][2]:.4f}
endloop
endfacet
"""

class ASCII_STL_Writer:
    """ Export 3D objects build of 3 or 4 vertices as ASCII STL file.
    """
    def __init__(self, stream):
        self.fp = stream
        self._write_header()

    def _write_header(self):
        self.fp.write("solid python\n")

    def close(self):
        self.fp.write("endsolid python\n")

    def _write(self, face):
        self.fp.write(ASCII_FACET.format(face=face))

    def _split(self, face):
        p1, p2, p3, p4 = face
        return (p1, p2, p3), (p3, p4, p1)

    def add_face(self, face):
        """ Add one face with 3 or 4 vertices. """
        if len(face) == 4:
            face1, face2 = self._split(face)
            self._write(face1)
            self._write(face2)
        elif len(face) == 3:
            self._write(face)
        else:
            raise ValueError('only 3 or 4 vertices for each face')

    def add_faces(self, faces):
        """ Add many faces. """
        for face in faces:
            self.add_face(face)

class RandomMeshStructure:
    def torus_dist2(self, p1, p2, w, h):
        return min(abs(p1.x - p2.x), w - abs(p1.x - p2.x))**2 + min(abs(p1.y - p2.y), h - abs(p1.y-p2.y))**2

    def get_object(self, shrink_offset=0, seed=None):
        if not seed:
            seed = self.seed
        if not seed:
            seed = 0
        random.seed( seed )

        width = self.avg_rad * 2 * math.pi
        points = []

        #Put points along top and bottom
        edge_count = int(math.floor(width / self.min_point_dist))
        edge_width = width / edge_count
        for i in range(edge_count):
            points.append( Vec3( edge_width*i, 0 ) )
            points.append( Vec3( edge_width*i, self.height ) )

        #Fill the area with points
        while(True):
            found = False
            for i in xrange(1000):
                point = Vec3(random.uniform(0, width), random.uniform(0, self.height))
                collides = False
                for p in points:
                    if self.torus_dist2( point, p, width, self.height ) < self.min_point_dist**2:
                        collides = True
                        break

                if not collides:
                    points.append( point )
                    found = True
                    break

            if not found:
                break

        def realp(point):
            dist = self.calc(point.x/width, point.y/self.height)
            a = -point.x/width * math.pi * 2
            return Vec3( math.cos( a ) * dist, math.sin( a ) * dist, point.y )
        real_points = [realp(p) for p in points]

        tri = Delaunay([p.to_list()[:2] for p in points], qhull_options='Qt')

        with open('vase/test.stl', 'wb') as fp:
            writer = ASCII_STL_Writer(fp)
            writer.add_faces( [ [real_points[t[0]], real_points[t[1]], real_points[t[2]]] for t in tri.simplices ] )
            writer.close()

        return polyhedron( points=[p.to_list() for p in real_points], faces=[[t[0], t[1], t[2]] for t in tri.simplices] )
