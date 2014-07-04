from solid import *
from solid.utils import *

class Vec3:
	
	def __init__( self, x=0, y=0, z=0 ):
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)
	
	def length( self ):
		return math.sqrt( self.length2() )
	
	def length2( self ):
		return self.x*self.x + self.y*self.y + self.z*self.z
	
	def to_list( self ):
		return [self.x,self.y,self.z]
	
	def distance( self, other ):
		return math.sqrt( self.distance2( other ) )
	
	def copy( self ):
		return Vec3( self.x, self.y, self.z )
	
	def distance2( self, other ):	
		x = self.x - other.x
		y = self.y - other.y
		z = self.z - other.z
		return x*x+y*y+z*z
	
	def normalize( self ):
		len = self.length()
		if len == 0:
			return
		self /= len
		return self
	
	def dot( self, vec ):
		return self.x*vec.x + self.y*vec.y + self.z*vec.z
	
	def rotate( self, axis, angle ):
		axis = axis.copy().normalize()
		vnorm = self.copy().normalize()
		_parallel = axis.dot( self )
		parallel = axis * _parallel
		perp = self - parallel
		cross = self.cross( axis )
		result = parallel + cross * math.sin( -angle ) + perp * math.cos( -angle )
		return result
	
	def cross( self, v ):
		cross_x = self.y * v.z - v.y * self.z;
		cross_y = self.z * v.x - v.z * self.x;
		cross_z = self.x * v.y - v.x * self.y;
		return Vec3( cross_x, cross_y, cross_z )
	
	def __add__( self, other ):
		return Vec3( self.x + other.x, self.y + other.y, self.z + other.z )
	
	def __sub__( self, other ):
		return Vec3( self.x - other.x, self.y - other.y, self.z - other.z )
		
	def __mul__( self, val ):
		return Vec3( self.x * val, self.y * val, self.z * val )
		
	def __iadd__( self, other ):
		self.x += other.x
		self.y += other.y
		self.z += other.z
		return self
	
	def __imul__( self, val ):
		self.x *= val
		self.y *= val
		self.z *= val
		return self
	
	def __idiv__( self, val ):
		self.x /= val
		self.y /= val
		self.z /= val
		return self
	
	def __getitem__( self, key ):
		if key == 0:
			return self.x
		elif key == 1:
			return self.y
		elif key == 2:
			return self.z
		else:
			raise Exception("Invalid index to Vec3")
        
	def __setitem__( self, key, value ):
		if key == 0:
			self.x = value
		elif key == 1:
			self.y = valye
		elif key == 2:
			self.z = value
		else:
			raise Exception("Invalid index to Vec3")
        
	def __str__( self ):
		return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

def make_trunk( height, sections, pf, index=False ):
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
			if index:
				points.append( pf( h, s ) )
			else:
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