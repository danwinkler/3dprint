from solid import *
from zack.lib.mat import *

# A pathMat is a list of orthonormal Mat4's
def pathToPathMat( path ):
	pathMat = []
	for i in xrange(0, len(path) ):
		if i == len(path)-1:
			z = Vec3( path[i] )
			z.sub( path[i-1] )
		else:
			z = Vec3( path[i+1] )
			z.sub( path[i] )
		z.normalize()
		
		y = Vec3( path[i] )
		y.cross( z )
		y.normalize()
		
		x = Vec3( z )
		x.cross( y )

		m = Mat4( [ [x.x,y.x,z.x,path[i].x], [x.y,y.y,z.y,path[i].y], [x.z,y.z,z.z,path[i].z], [0,0,0,1] ] )
		pathMat.append( m )

	return pathMat

def interpolate( p, pathMat ):
	totalPathLen = 0
	for i in xrange(1, len(pathMat) ):
		p0 = Vec3( pathMat[i-1].getTrans() )
		p1 = Vec3( pathMat[i+0].getTrans() )
		p1.sub( p0 )
		totalPathLen += p1.mag()

	q = p * totalPathLen

	pathLen = 0
	lastPathLen = 0
	for i in xrange(1, len(pathMat) ):
		p0 = Vec3( pathMat[i-1].getTrans() )
		p1 = Vec3( pathMat[i+0].getTrans() )
		p1.sub( p0 )
		p1mag = p1.mag()
		if pathLen+p1mag > q:
			frac = ( q - lastPathLen ) / p1mag
			p1.mul( frac )
			p2 = Vec3( p0 )
			p2.add( p1 )
			m = Mat4( pathMat[i-1] )
			m.setTrans( p2 )
			return m

		pathLen += p1mag
		lastPathLen = pathLen

	return Mat4( pathMat[len(pathMat)-1] )


def extrudeTubeAlongPath( radialSteps, heightSteps, pathMat, radius, radialFunc=None ):
	verts = []
	for i in xrange(0,heightSteps):
		m = interpolate( float(i)/float(heightSteps), pathMat ) 

		for j in xrange(0,radialSteps):
			if radialFunc:
				p1 = radialFunc( i, heightSteps, j, radialSteps )
			else:
				t = 3.14*2 * j / float(radialSteps)
				p1 = Vec3( [ radius * cos(t), radius * sin(t), 0 ] )

			p2 = m.mul( p1 )
			verts.append( p2.list() )

	# In case the end is not convex, we need a center vertex, AVERAGE the ends
	p1 = Vec3()
	p2 = Vec3()
	for j in xrange(0,radialSteps):
		p1.add( verts[j] )
		p2.add( verts[heightSteps*radialSteps-1-j] )
	p1.mul( 1.0 / float(radialSteps) )
	p2.mul( 1.0 / float(radialSteps) )
	verts.append( p1.list() )
	verts.append( p2.list() )

	triangles = []
	for i in xrange(0,heightSteps-1):
		for a in xrange(0,radialSteps):
			f1 = [ radialSteps*i+a, radialSteps*i+(a+1)%radialSteps, radialSteps*(i+1)+a ]
			triangles.append( f1 )

			f2 = [ radialSteps*i+(a+1)%radialSteps, radialSteps*(i+1)+(a+1)%radialSteps, radialSteps*(i+1)+a ]
			triangles.append( f2 )

	p1 = len(verts)-2
	for a in xrange(0,radialSteps):
		f1 = [ (a+1)%radialSteps, (a+0)%radialSteps, p1 ]
		triangles.append( f1 )

	p2 = len(verts)-1
	for a in xrange(0,radialSteps):
		f1 = [ p2, (heightSteps-1)*radialSteps+(a+0)%radialSteps, (heightSteps-1)*radialSteps+(a+1)%radialSteps ]
		triangles.append( f1 )

	return polyhedron( verts, triangles )
