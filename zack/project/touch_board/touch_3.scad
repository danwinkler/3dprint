union() {
	translate( [ 0, 0, +0 ] )
	difference() {
		cylinder( r=50, h=3, $fn=64 );
		translate( [ 0, 0, -1 ] )
		cylinder( r=45, h=10, $fn=64 );
	}
	
	union() {
		translate( [ 0, 0, -1 ] )
		cylinder( r=50, h=2, $fn=64 );
		intersection() {
			cylinder( r=50, h=20, $fn=64 );
			for( x=[-50:11:50] ) {
				translate( [ -50, x, 0 ] )
				rotate( 90, [0,1,0] )
				cylinder( r=3, h=100, $fn=16 );
			}
		}
	}
}
