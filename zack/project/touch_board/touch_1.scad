union() {
	translate( [ 0, 0, +5 ] )
	difference() {
		cylinder( r=50, h=3, $fn=64 );
		translate( [ 0, 0, -1 ] )
		cylinder( r=45, h=10, $fn=64 );
	}
	
	union() {
		translate( [ 0, 0, 8 ] )
		cylinder( r=50, h=2, $fn=64 );
		intersection() {
			cylinder( r=50, h=8, $fn=64 );
			for( y=[-50:8:50] ) {
				for( x=[-50:8:50] ) {
					translate( [ x, y, 8 ] )
					sphere( r=3, $fn=16 );
				}
			}
		}
	}
}