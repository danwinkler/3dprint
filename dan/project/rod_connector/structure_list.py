from structure_class import *
import math
import random

class S1(LayerStructure):
    hscale = 300
    height = 10
    sections = 6
    def calc(self, h, a):
        offset = math.pi * .125
        angle_minus_offset = (math.pi*2 / self.sections) * a
        angle = angle_minus_offset + offset * h
        dist = (500 - h*30) + (150 if a % 2 == 0 else -100)
        return angle, dist

class S2(LayerStructure):
    hscale = 300
    height = 10
    sections = 6
    def calc(self, h, a):
        offset = math.pi * .125
        angle_minus_offset = (math.pi*2 / self.sections) * a
        angle = angle_minus_offset + offset * h
        dist = (500 - h*30) + math.cos( angle_minus_offset * 2 ) * 150
        return angle, dist

class S3(LayerStructure):
    hscale = 300
    height = 10
    sections = 6
    def calc(self, h, a):
        offset = math.pi * .125
        angle_minus_offset = (math.pi*2 / self.sections) * a
        angle = angle_minus_offset + offset * h
        dist = (500 - h*30) + math.cos( angle_minus_offset ) * 200
        return angle, dist

class S4(LayerStructure):
    hscale = 300
    height = 10
    sections = 6
    def calc(self, h, a):
        offset = math.pi * .125
        angle_minus_offset = (math.pi*2 / self.sections) * a
        angle = angle_minus_offset + offset * h
        dist = (500 - h*30) - math.cos( angle_minus_offset * 2 ) * 150
        return angle, dist

class S5(LayerStructure):
    hscale = 300
    height = 10
    sections = 6
    def calc(self, h, a):
        offset = math.pi * .125
        angle_minus_offset = (math.pi*2 / self.sections) * a
        angle = angle_minus_offset + offset * h
        height = float(h) / float(self.height)
        height *= math.pi
        dist = (500 - math.sin(height)*250 + h**3 * .6)
        return angle, dist

class S6(LayerStructure):
    hscale = 300
    height = 10
    sections = 6
    def calc(self, h, a):
        offset = math.pi * .125
        angle_minus_offset = (math.pi*2 / self.sections) * a
        angle = angle_minus_offset + offset * h
        dist = (500 - h*30) + (100 if a % 3 == 0 else 0)
        hscale = 300
        return angle, dist

class S7(LayerStructure):
    hscale = 300
    height = 10
    sections = 6
    def calc(self, h, a):
        offset = math.pi * .125
        angle_minus_offset = (math.pi*2 / self.sections) * a
        angle = angle_minus_offset + offset * h
        dist = (500 - abs(h)*30)
        return angle, dist

class RandS1(RandomMeshStructure):
    seed = 1
    min_point_dist = 1000
    height = 3000
    avg_rad = 500
    def calc(self, x, y):
        a = x * math.pi
        h = y * 10
        offset = math.pi * .125
        angle_minus_offset = (math.pi*2 / 6) * a
        angle = angle_minus_offset + offset * h
        dist = (500 - h*40) + math.sin( y*20+x*20 ) * 60 + 50
        return dist

class WP1(WallPiece):
    width = 1000
    height = 1000

    points = [Vec3(random.uniform(0, 1000), random.uniform(0, 1000), random.uniform(0, 100)) for i in range(100)]
    points += [Vec3(0, i*100, 100) for i in range( 11 )]
    points += [Vec3(i*100, 0, 100) for i in range( 11 )]
    points += [Vec3(1000, i*100, 100) for i in range( 11 )]
    points += [Vec3(i*100, 1000, 100) for i in range( 11 )]

    sx_points = range(100, 111)
    sy_points = range(111, 122)
    bx_points = range(122, 133)
    by_points = range(133, 144)
