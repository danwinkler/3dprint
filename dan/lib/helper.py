from solid import *
from solid.utils import *

def make_trunk( height, sections, pf ):
	def add_points( p1, p2 ):
		return [p1[0]+p2[0],p1[1]+p2[1],p1[2]+p2[2]]

	def scale_point( p, s ):
		return [p[0]*s,p[1]*s,p[2]*s]	
	
	points = []
	triangles = []
	
	max = height*sections
	
	#generate points
	for h in range(height):
		for s in range(sections):
			points.append( pf( h/float(height), s/float(sections) ) )
	
	for h in range(height-1):
		h2 = h+1
		for s in range(sections):
			s2 = (s+1) % sections
			
			# c------d
			# |  \   |
			# |   \  |
			# a------b
			
			a = h*sections + s
			b = h*sections + s2
			c = h2*sections + s
			d = h2*sections + s2
			
			triangles.append( [a,c,b] )
			triangles.append( [b,c,d] )
	
	bottom_avg = [0,0,0]
	top_avg = [0,0,0]
	for s in range( sections ):
		bottom_avg = add_points( bottom_avg, points[s] )
		top_avg = add_points( top_avg, points[((height-1)*sections)+s] )
		
	bottom_avg = scale_point( bottom_avg, 1.0 / sections )
	top_avg = scale_point( top_avg, 1.0 / sections )
	
	points.append( bottom_avg )
	points.append( top_avg )
	
	for s in range( sections ):
		s2 = (s+1) % sections
		triangles.append( [s2,max,s] )
		triangles.append( [((height-1)*sections)+s,max+1,((height-1)*sections)+s2] )
	
	return polyhedron( points=points, triangles=triangles )