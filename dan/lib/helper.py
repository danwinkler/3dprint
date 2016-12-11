from solid import *
from solid.utils import *

import random

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

	def __repr__( self ):
		return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

#Find distance from point p to line segment
def point_to_line_segment( p, l0, l1 ):
	v = l1 - l0
	w = p - l0

	c1 = w.dot( v )
	if c1 < 0:
		return p.distance( l0 )

	c2 = v.dot( v )
	if c2 < c1:
		return p.distance( l1 )

	b = c1 / c2
	pb = l0 + v * b
	return p.distance( pb )

#Find distance**2 from point p to line segment
def point_to_line_segment_2( p, l0, l1 ):
	v = l1 - l0
	w = p - l0

	c1 = w.dot( v )
	if c1 < 0:
		return p.distance2( l0 )

	c2 = v.dot( v )
	if c2 < c1:
		return p.distance2( l1 )

	b = c1 / c2
	pb = l0 + v * b
	return p.distance2( pb )

#http://www.wyrmtale.com/blog/2013/115/2d-line-intersection-in-c
def line_line_intersect_2d( ps1, pe1, ps2, pe2 ):
	# Get A,B,C of first line - points : ps1 to pe1
	A1 = pe1.y-ps1.y
	B1 = ps1.x-pe1.x
	C1 = A1*ps1.x+B1*ps1.y

	# Get A,B,C of second line - points : ps2 to pe2
	A2 = pe2.y-ps2.y
	B2 = ps2.x-pe2.x
	C2 = A2*ps2.x+B2*ps2.y

	# Get delta and check if the lines are parallel
	delta = A1*B2 - A2*B1
	if delta == 0:
		raise ArithmeticError( "Lines are parallel" )

	# now return the Vector2 intersection point
	return Vec3( (B2*C1 - B1*C2)/delta, (A1*C2 - A2*C1)/delta )


def cyl_on_vec( v, r=1 ):
	v = v.copy()
	length = v.length()
	v.normalize()
	up_vec = Vec3( 0, 0, 1 )
	cross = up_vec.cross( v )
	angle = math.acos( up_vec.dot( v ) )
	return rotate( a=math.degrees( angle ), v=cross.to_list() ) (
		cylinder( h=length, r=r )
	)

def rot_on_vec( v, obj ):
	v = v.copy()
	length = v.length()
	v.normalize()
	up_vec = Vec3( .000001, .000001, 1 )
	cross = up_vec.cross( v )
	angle = math.acos( up_vec.dot( v ) )
	return rotate( a=math.degrees( angle ), v=cross.to_list() ) (
		obj
	)

#Given a list of points and a width function,
#generates a "vine" polyhedron using make_trunk
# points - a list of Vec3's
# wf - a function that returns the distance from the point,
#      given the point index and the angle
# sections - the number of points around the circle
def vine( points, wf, sections=8 ):
	global cross

	cross = points[0].copy()
	cross.x += random.uniform( -.5, .5 )
	cross.y += random.uniform( -.5, .5 )
	cross.z += random.uniform( -.5, .5 )

	def tf( h, a ):
		global cross
		if h == 0:
			vec = points[1] - points[0]
		elif h == len(points)-1:
			vec = points[-1] - points[-2]
		else:
			vec = (points[h] - points[h-1]) + (points[h+1] - points[h])

		vec.normalize()

		angle = (a/float(sections)) * math.pi * 2

		p = vec.cross( cross )

		p = p.cross( vec )

		cross = p
		cross.normalize()

		p = p.rotate( vec, angle )

		width = wf( h, angle )

		return [points[h].x + p.x * width, points[h].y + p.y * width, points[h].z + p.z * width]

	return make_trunk( len( points ), sections, tf, index=True )

# Returns a polyhedron based on a set of points
# height - number of rows of points
# sections - number of points around each row (in a circle)
# pf - a function, that when given a height and a section number, returns a list [x,y,z]
# index - When false, pf is called with height and sections as floats between 0...1
#         When true, calls pf with the index (0...n)
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
				points.append( pf( h/float(height-1), s/float(sections) ) )

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

	return polyhedron( points=points, faces=triangles )
