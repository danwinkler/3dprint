from math import *
import copy

class Vec3:
	def __init__( self, v=None ):
		if v is None:
			self.x = 0
			self.y = 0
			self.z = 0

		if type(v) is list:
			self.x = copy.copy( v[0] )
			self.y = copy.copy( v[1] )
			self.z = copy.copy( v[2] )

		if isinstance(v,Vec3):
			self.x = copy.copy( v.x )
			self.y = copy.copy( v.y )
			self.z = copy.copy( v.z )

	def origin(self):
		self.x = 0
		self.y = 0
		self.z = 0

	def cross( self, b ):
		assert( isinstance(b,Vec3) )
		_x = self.y*b.z - self.z*b.y
		_y = self.z*b.x - self.x*b.z
		_z = self.x*b.y - self.y*b.x
		self.x = _x
		self.y = _y
		self.z = _z

	def add( self, b ):
		if type(b) is list:
			self.x += b[0]
			self.y += b[1]
			self.z += b[2]

		if isinstance(b,Vec3):
			self.x += b.x
			self.y += b.y
			self.z += b.z

	def sub( self, b ):
		if type(b) is list:
			self.x -= b[0]
			self.y -= b[1]
			self.z -= b[2]

		if isinstance(b,Vec3):
			self.x -= b.x
			self.y -= b.y
			self.z -= b.z

	def mul( self, b ):
		self.x *= b
		self.y *= b
		self.z *= b

	def div( self, b ):
		self.x /= b
		self.y /= b
		self.z /= b

	def mag2( self ):
		return self.x * self.x + self.y * self.y + self.z * self.z

	def mag( self ):
		return sqrt( self.x * self.x + self.y * self.y + self.z * self.z )

	def dot( self, b ):
		assert( isinstance(b,Vec3) )
		return self.x * b.x + self.y * b.y + self.z * b.z

	def normalize( self ):
		m = self.mag()
		if m > 0:
			self.x /= m
			self.y /= m
			self.z /= m

	def list( self ):
		return [ self.x, self.y, self.z ]


class Mat4:
	def __init__( self, m=None ):
		if m is None:
			self.identity()

		if type(m) is list:
			self.m = copy.deepcopy(m)

		if isinstance(m,Mat4):
			self.m = copy.deepcopy(m.m)

	def list( self ):
		return self.m

	def cat( self, b ):
		assert( isinstance(b,Mat4) )
		t = Mat4()
		t.m[0][0] = self.m[0][0]*b.m[0][0] + self.m[1][0]*b.m[0][1] + self.m[2][0]*b.m[0][2] + self.m[3][0]*b.m[0][3]
		t.m[0][1] = self.m[0][1]*b.m[0][0] + self.m[1][1]*b.m[0][1] + self.m[2][1]*b.m[0][2] + self.m[3][1]*b.m[0][3]
		t.m[0][2] = self.m[0][2]*b.m[0][0] + self.m[1][2]*b.m[0][1] + self.m[2][2]*b.m[0][2] + self.m[3][2]*b.m[0][3]
		t.m[0][3] = self.m[0][3]*b.m[0][0] + self.m[1][3]*b.m[0][1] + self.m[2][3]*b.m[0][2] + self.m[3][3]*b.m[0][3]

		t.m[1][0] = self.m[0][0]*b.m[1][0] + self.m[1][0]*b.m[1][1] + self.m[2][0]*b.m[1][2] + self.m[3][0]*b.m[1][3]
		t.m[1][1] = self.m[0][1]*b.m[1][0] + self.m[1][1]*b.m[1][1] + self.m[2][1]*b.m[1][2] + self.m[3][1]*b.m[1][3]
		t.m[1][2] = self.m[0][2]*b.m[1][0] + self.m[1][2]*b.m[1][1] + self.m[2][2]*b.m[1][2] + self.m[3][2]*b.m[1][3]
		t.m[1][3] = self.m[0][3]*b.m[1][0] + self.m[1][3]*b.m[1][1] + self.m[2][3]*b.m[1][2] + self.m[3][3]*b.m[1][3]

		t.m[2][0] = self.m[0][0]*b.m[2][0] + self.m[1][0]*b.m[2][1] + self.m[2][0]*b.m[2][2] + self.m[3][0]*b.m[2][3]
		t.m[2][1] = self.m[0][1]*b.m[2][0] + self.m[1][1]*b.m[2][1] + self.m[2][1]*b.m[2][2] + self.m[3][1]*b.m[2][3]
		t.m[2][2] = self.m[0][2]*b.m[2][0] + self.m[1][2]*b.m[2][1] + self.m[2][2]*b.m[2][2] + self.m[3][2]*b.m[2][3]
		t.m[2][3] = self.m[0][3]*b.m[2][0] + self.m[1][3]*b.m[2][1] + self.m[2][3]*b.m[2][2] + self.m[3][3]*b.m[2][3]

		t.m[3][0] = self.m[0][0]*b.m[3][0] + self.m[1][0]*b.m[3][1] + self.m[2][0]*b.m[3][2] + self.m[3][0]*b.m[3][3]
		t.m[3][1] = self.m[0][1]*b.m[3][0] + self.m[1][1]*b.m[3][1] + self.m[2][1]*b.m[3][2] + self.m[3][1]*b.m[3][3]
		t.m[3][2] = self.m[0][2]*b.m[3][0] + self.m[1][2]*b.m[3][1] + self.m[2][2]*b.m[3][2] + self.m[3][2]*b.m[3][3]
		t.m[3][3] = self.m[0][3]*b.m[3][0] + self.m[1][3]*b.m[3][1] + self.m[2][3]*b.m[3][2] + self.m[3][3]*b.m[3][3]
		self.m = t.m


	def add( b ):
		assert( isinstance(b,Mat4) )

		self.m[0][0] += b.m[0][0];
		self.m[0][1] += b.m[0][1];
		self.m[0][2] += b.m[0][2];
		self.m[0][3] += b.m[0][3];

		self.m[1][0] += b.m[1][0];
		self.m[1][1] += b.m[1][1];
		self.m[1][2] += b.m[1][2];
		self.m[1][3] += b.m[1][3];

		self.m[2][0] += b.m[2][0];
		self.m[2][1] += b.m[2][1];
		self.m[2][2] += b.m[2][2];
		self.m[2][3] += b.m[2][3];

		self.m[3][0] += b.m[3][0];
		self.m[3][1] += b.m[3][1];
		self.m[3][2] += b.m[3][2];
		self.m[3][3] += b.m[3][3];

	def mul( self, b ):
		if type(b) is float:
			self.m[0][0] *= b
			self.m[0][1] *= b
			self.m[0][2] *= b
			self.m[0][3] *= b

			self.m[1][0] *= b
			self.m[1][1] *= b
			self.m[1][2] *= b
			self.m[1][3] *= b

			self.m[2][0] *= b
			self.m[2][1] *= b
			self.m[2][2] *= b
			self.m[2][3] *= b

			self.m[3][0] *= b
			self.m[3][1] *= b
			self.m[3][2] *= b
			self.m[3][3] *= b

		if type(b) is list:
			b = Vec3( b )
			# Fall through

		if isinstance(b,Vec3):
			t = Vec3()
			t.x = b.x*self.m[0][0] + b.y*self.m[0][1] + b.z*self.m[0][2] + self.m[0][3]
			t.y = b.x*self.m[1][0] + b.y*self.m[1][1] + b.z*self.m[1][2] + self.m[1][3]
			t.z = b.x*self.m[2][0] + b.y*self.m[2][1] + b.z*self.m[2][2] + self.m[2][3]
			return t

	def identity( self ):
		self.m = [ 0, 0, 0, 0 ]
		self.m[0] = [0] * 4
		self.m[1] = [0] * 4
		self.m[2] = [0] * 4
		self.m[3] = [0] * 4
		self.m[0][0] = 1
		self.m[1][1] = 1
		self.m[2][2] = 1
		self.m[3][3] = 1

	def getTrans( self ):
		return Vec3( [ self.m[0][3], self.m[1][3], self.m[2][3] ] )

	def setTrans( self, v ):
		self.m[0][3] = v.x
		self.m[1][3] = v.y
		self.m[2][3] = v.z

	def trans( self, v ):
		assert( isinstance(v,Vec3) )
		self.m[0][3] += v.x
		self.m[1][3] += v.y
		self.m[2][3] += v.z

	def transpose( self ):
		t = Mat4();
		t.m[0][0] = self.m[0][0];
		t.m[0][1] = self.m[1][0];
		t.m[0][2] = self.m[2][0];
		t.m[0][3] = self.m[3][0];

		t.m[1][0] = self.m[0][1];
		t.m[1][1] = self.m[1][1];
		t.m[1][2] = self.m[2][1];
		t.m[1][3] = self.m[3][1];

		t.m[2][0] = self.m[0][2];
		t.m[2][1] = self.m[1][2];
		t.m[2][2] = self.m[2][2];
		t.m[2][3] = self.m[3][2];

		t.m[3][0] = self.m[0][3];
		t.m[3][1] = self.m[1][3];
		t.m[3][2] = self.m[2][3];
		t.m[3][3] = self.m[3][3];

		self.m = t.m

	def orthoNormalize( self ):
		x = Vec3( [ self.m[0][0], self.m[0][1], self.m[0][2] ] );
		y = Vec3( [ self.m[1][0], self.m[1][1], self.m[1][2] ] );
		z = Vec3();
		x.normalize();

		z = x;
		z.cross( y );
		z.normalize();

		y = z;
		y.cross( x );
		y.normalize();

		self.m[0][0] = x.x;
		self.m[1][0] = y.x;
		self.m[2][0] = z.x;
		self.m[0][1] = x.y;
		self.m[1][1] = y.y;
		self.m[2][1] = z.y;
		self.m[0][2] = x.z;
		self.m[1][2] = y.z;
		self.m[2][2] = z.z;


	def inverse( self ):
		# Stolen from bump.c - David G Yu, SGI
		tmp = [ 0, 0, 0, 0 ]
		tmp[0] = [0] * 4
		tmp[1] = [0] * 4
		tmp[2] = [0] * 4
		tmp[3] = [0] * 4

		aug = [ 0, 0, 0, 0, 0 ]
		tmp[0] = [0] * 4
		tmp[1] = [0] * 4
		tmp[2] = [0] * 4
		tmp[3] = [0] * 4
		tmp[4] = [0] * 4

		for h in xrange(0,4):
			for i in xrange(0,4):
				aug[0][i] = self.m[0][i]
				aug[1][i] = self.m[1][i]
				aug[2][i] = self.m[2][i]
				aug[3][i] = self.m[3][i]
				aug[4][i] = 1 if h == i else 0

			for i in xrange(0,3):
				pivot = 0

				pivotIndex = 0
				for j in xrange(i,4):
					temp = aug[i][j] if aug[i][j] > 0 else -aug[i][j]
					if pivot < temp:
						pivot = temp;
						pivotIndex = j

				if pivot == 0:
					self.identity()
					return False

				if pivotIndex != i:
					for k in xrange(i,5):
						temp = aug[k][i]
						aug[k][i] = aug[k][pivotIndex]
						aug[k][pivotIndex] = temp

				for k in xrange(i+1,4):
					q = -aug[i][k] / aug[i][i]
					aug[i][k] = 0
					for j in xrange(i+1,5):
						aug[j][k] = q * aug[j][i] + aug[j][k]

			if aug[3][3] == 0:
				self.identity();
				return False

			tmp[h][3] = aug[4][3] / aug[3][3]

			for k in xrange(1,4):
				q = 0
				for j in xrange(1,k+1):
					q += aug[4-j][3-k] * tmp[h][4-j]
				
				tmp[h][3-k] = (aug[4][3-k] - q) / aug[3-k][3-k]

		self.m[0] = tmp[0]
		self.m[1] = tmp[1]
		self.m[2] = tmp[2]
		self.m[3] = tmp[3]

		return True


def rotate3D( axis, angle_rad ):
	if type(axis) is list:
		axis = Vec3( axis )
	else:
		assert( isinstance(axis,Vec3) )

	assert( type(angle_rad) is float or type(angle_rad) is int )
	
	c = cos( angle_rad )
	s = sin( angle_rad )
	t = 1.0 - c

	axis.normalize()

	mat = Mat4()
	mat.m[0][0] = t * axis.x * axis.x + c
	mat.m[1][0] = t * axis.x * axis.y - s * axis.z
	mat.m[2][0] = t * axis.x * axis.z + s * axis.y
	mat.m[3][0] = 0.0

	mat.m[0][1] = t * axis.x * axis.y + s * axis.z
	mat.m[1][1] = t * axis.y * axis.y + c
	mat.m[2][1] = t * axis.y * axis.z - s * axis.x
	mat.m[3][1] = 0.0

	mat.m[0][2] = t * axis.x * axis.z - s * axis.y
	mat.m[1][2] = t * axis.y * axis.z + s * axis.x
	mat.m[2][2] = t * axis.z * axis.z + c
	mat.m[3][2] = 0.0

	mat.m[0][3] = 0.0
	mat.m[1][3] = 0.0
	mat.m[2][3] = 0.0
	mat.m[3][3] = 1.0

	return mat


def trans3D( v ):
	if type(v) is list:
		mat = Mat4()
		mat.m[0][3] = v[0]
		mat.m[1][3] = v[1]
		mat.m[2][3] = v[2]
		return mat
	
	if isinstance(v,Vec3):
		mat = Mat4()
		mat.m[0][3] = v.x
		mat.m[1][3] = v.y
		mat.m[2][3] = v.z
		return mat

	assert( False )

def scale3D( v ):
	if type(v) is float or type(v) is int:
		mat = Mat4()
		mat.m[0][0] = v
		mat.m[1][1] = v
		mat.m[2][2] = v
		return mat

	if type(v) is list:
		mat = Mat4()
		mat.m[0][0] = v[0]
		mat.m[1][1] = v[1]
		mat.m[2][2] = v[2]
		return mat

	if isinstance(v,Vec3):
		mat = Mat4()
		mat.m[0][0] = v.x
		mat.m[1][1] = v.y
		mat.m[2][2] = v.z
		return mat

	assert( False )
